#!/usr/bin/env python3
"""AZURAVEL 1.0: strict lexicon, S+L permutation grammar, Code 128-B.

Standard-library runtime. Source of truth: AZURAVEL_DATA.json.
Physical scan verification is external (tests use pyzbar when present).
"""
from __future__ import annotations
import json
import re
import html
from pathlib import Path

DATA=json.loads(Path(__file__).with_name('AZURAVEL_DATA.json').read_text(encoding='utf-8'))
ENTRIES=DATA['entries']; BY_ID={e['id']:e for e in ENTRIES}; ROOTS={e['root']:e for e in ENTRIES}
FORM={f['word']:(e,f) for e in ENTRIES for f in e['forms']}
CONSONANTS=DATA['root_consonants']; VOWELS=DATA['vowels']; PARTICLES=DATA['particles']
SYMBOL_PATTERNS=DATA['code128_patterns']
ROLE_TO_STATE={s['role']:s for s in DATA['states']}
PRONOUNS={'ya','ye','yi','yo','yu'}
TOKEN_RE=re.compile(r'[a-z]+|[.?!;]')

class AzuravelError(ValueError):pass

def syllables(word:str)->list[str]:
 if not isinstance(word,str) or not re.fullmatch(r'[a-z]{6}',word):raise AzuravelError('A lexical form must contain three CV syllables (six lowercase letters).')
 chunks=[word[i:i+2] for i in (0,2,4)]
 if any(x[0] not in CONSONANTS or x[1] not in VOWELS for x in chunks):raise AzuravelError('Root syllables must be CV with an allowed root consonant and vowel.')
 if len({x[0] for x in chunks})!=3:raise AzuravelError('The three root consonants must be different.')
 return chunks

def canonical(word:str)->str:
 return ''.join(sorted(syllables(word),key=lambda x:CONSONANTS.index(x[0])))

def transform(root:str,s:int,r:int)->str:
 if s not in (0,1) or r not in (0,1,2):raise AzuravelError('S must be 0/1 and L must be 0/1/2.')
 if canonical(root)!=root:raise AzuravelError('Input must be canonical (sorted consonants).')
 chunks=syllables(root)
 if s:chunks[0],chunks[1]=chunks[1],chunks[0]
 return ''.join(chunks[r:]+chunks[:r])

def inspect_word(word:str)->dict:
 c=canonical(word)
 if c not in ROOTS:raise AzuravelError(f'Unknown root bag {c!r}; no lexical item is authorized.')
 entry=ROOTS[c]
 f=next((form for form in entry['forms'] if form['word']==word),None)
 if f is None:raise AzuravelError('Illegal permutation.')
 return {'id':entry['id'],'root':c,'surface':word,'concept':entry['concept'],'domain':entry['domain'],**f}

def pronunciation(phrase:str)->str:
 out=[]
 for tok in lex(phrase):
  if tok in '.?!;':out.append(tok);continue
  if tok not in PARTICLES and tok not in FORM:raise AzuravelError(f'Unknown token: {tok}')
  phon=''.join('ɾ' if ch=='r' else 'j' if ch=='y' else ch for ch in tok)
  if len(tok)==6:phon=phon[:2]+'ˈ'+phon[2:]
  out.append(phon)
 return '/'+ ' '.join(out) +'/'

def lex(phrase:str)->list[str]:
 if not isinstance(phrase,str) or not phrase.strip():raise AzuravelError('Sentence is empty.')
 if re.sub(r'[a-z.?!;\s]','',phrase):raise AzuravelError('Sentence contains unsupported characters (lowercase Romanization only).')
 tokens=TOKEN_RE.findall(phrase)
 if not tokens:raise AzuravelError('No tokens supplied.')
 return tokens

def payload(word:str)->str:
 a=inspect_word(word)
 return f"AZ1|{a['id']}|{a['state'][0]}|{a['state'][1]}|{word}"

def decode_payload(string:str)->dict:
 if not isinstance(string,str) or not re.fullmatch(r'AZ1\|[A-Z][0-9]{2}\|[01]\|[012]\|[a-z]{6}',string):
  raise AzuravelError('Invalid AZ1 payload layout or version.')
 _,id_,s,r,word=string.split('|')
 if id_ not in BY_ID:raise AzuravelError('Unknown lexical ID.')
 expected=transform(BY_ID[id_]['root'],int(s),int(r))
 if word!=expected:raise AzuravelError(f'ID/state/surface mismatch; expected {expected}.')
 return inspect_word(word)

def code128_symbols(text:str)->list[int]:
 if not isinstance(text,str) or not text or any(not (32<=ord(c)<=126) for c in text):raise AzuravelError('Code 128-B payload must contain printable 7-bit ASCII.')
 chars=[ord(ch)-32 for ch in text]
 check=(104+sum((index+1)*sym for index,sym in enumerate(chars)))%103
 return [104]+chars+[check,106]

def symbol_bits(code:int)->str:
 widths=SYMBOL_PATTERNS[code]
 return ''.join(str(int(i%2==0))*int(n) for i,n in enumerate(widths))

def barcode_bits(text:str)->str:
 return '0'*10 + ''.join(symbol_bits(sym) for sym in code128_symbols(text))+'0'*10

def decode_barcode_bits(bits:str)->str:
 if not isinstance(bits,str) or not re.fullmatch(r'[01]+',bits):raise AzuravelError('Module string must contain only 0/1.')
 left=len(bits)-len(bits.lstrip('0')); right=len(bits)-len(bits.rstrip('0'))
 if left<10 or right<10:raise AzuravelError('Code 128 quiet zones must each be at least ten X modules.')
 core=bits[left:len(bits)-right]
 if not core.endswith(symbol_bits(106)):raise AzuravelError('Invalid Code 128 stop pattern.')
 core=core[:-13]
 if len(core)%11!=0 or len(core)<33:raise AzuravelError('Invalid Code 128 symbol count or module widths.')
 lookup={symbol_bits(i):i for i in range(106)}
 symbols=[]
 for i in range(0,len(core),11):
  chunk=core[i:i+11]
  if chunk not in lookup:raise AzuravelError('Invalid 11-module Code 128 character.')
  symbols.append(lookup[chunk])
 if symbols[0]!=104:raise AzuravelError('This profile requires Code 128 start B.')
 if any(x>94 for x in symbols[1:-1]):raise AzuravelError('This profile disallows subset switches and function symbols.')
 if len(symbols[1:-1])==0:raise AzuravelError('No data symbols.')
 check=(104+sum(i*x for i,x in enumerate(symbols[1:-1],1)))%103
 if check!=symbols[-1]:raise AzuravelError('Code 128 checksum error.')
 return ''.join(chr(x+32) for x in symbols[1:-1])

def barcode_svg(text:str,x:int=3,h:int=100)->str:
 if not (isinstance(x,int) and x>=2 and isinstance(h,int) and h>=50):raise AzuravelError('For legible rendering use x>=2 px and h>=50 px.')
 b=barcode_bits(text);rects=[];i=0
 while i<len(b):
  if b[i]=='1':
   j=i+1
   while j<len(b) and b[j]=='1':j+=1
   rects.append(f'<rect x="{i*x}" y="0" width="{(j-i)*x}" height="{h}"/>');i=j
  else:i+=1
 return f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Code 128 barcode for {html.escape(text,quote=True)}" width="{len(b)*x}" height="{h}" viewBox="0 0 {len(b)*x} {h}"><rect width="100%" height="100%" fill="white"/><g fill="black">'+''.join(rects)+'</g></svg>'

def parse_np(tokens:list[str],i:int)->tuple[dict,int]:
 plural=False
 if i<len(tokens) and tokens[i]=='la':plural=True;i+=1
 if i>=len(tokens):raise AzuravelError('Expected a nominal after a case marker.')
 first=tokens[i]
 if first in PRONOUNS:
  if plural:raise AzuravelError('Pronouns already encode number; la cannot precede one.')
 elif first in FORM and FORM[first][1]['role'] in ('CONC','SRC','PAT','RES'):pass
 else:raise AzuravelError(f'{first!r} is not a nominal.')
 i+=1
 if i<len(tokens) and tokens[i]=='li':
  if plural:raise AzuravelError('AZ1 does not allow la before a possessor; attach number to a standalone noun.')
  i+=1
  if i>=len(tokens):raise AzuravelError('Possessive li needs a possessed head.')
  if tokens[i] not in FORM or FORM[tokens[i]][1]['role'] not in ('CONC','SRC','PAT','RES'):
   raise AzuravelError('Possessed head must be a nominal lexical form.')
  second=tokens[i];i+=1
  return {'possessor':first,'head':second,'plural':False},i
 return {'head':first,'plural':plural},i

def parse_simple(tokens:list[str])->dict:
 if not tokens:raise AzuravelError('Empty finite clause.')
 i=0;imperative=tokens[0]=='va'
 if imperative:i=1
 args={};
 for marker in (['no','di','lu'] if imperative else ['ta','no','di','lu']):
  if i<len(tokens) and tokens[i]==marker:
   i+=1;args[marker],i=parse_np(tokens,i)
 if not imperative and 'ta' not in args:raise AzuravelError('A declarative needs an explicit ta-actor in AZ1.')
 features={}
 for slot,values in [('tense',('mi','mu')),('aspect',('ne','nu')),('negation',('sa',)),('modality',('pa','pe')),('causative',('ko',)),('reciprocal',('lo',)),('emphasis',('ke',))]:
  if i<len(tokens) and tokens[i] in values:
   features[slot]=tokens[i];i+=1
 if i>=len(tokens):raise AzuravelError('Missing final predicate.')
 pred=tokens[i];i+=1
 if pred!='ra' and not (pred in FORM and FORM[pred][1]['role'] in ('EVT','CTR')):raise AzuravelError('Final predicate must be EVT, CTR, or ra.')
 question=False
 if i<len(tokens) and tokens[i]=='ri':question=True;i+=1
 if i!=len(tokens):raise AzuravelError('Unexpected token or out-of-order marker after predicate: '+' '.join(tokens[i:]))
 if pred=='ra':
  if imperative or 'no' not in args or any(x in features for x in ('aspect','causative','reciprocal')):
   raise AzuravelError('ra requires actor + complement and has no imperative/aspect/causative/reciprocal.')
 elif 'no' in args and 'causative' not in features:
  raise AzuravelError('A no-patient on a lexical event requires ko in AZ1.')
 if 'reciprocal' in features:
  actor=args.get('ta')
  if imperative or not actor or not (actor.get('plural') or actor['head'] in ('yi','yo')):
   raise AzuravelError('lo requires a plural explicit actor (la NP, yi, or yo).')
 return {'type':'simple','imperative':imperative,'args':args,'features':features,'predicate':pred,'question':question}

def parse_sentence(src:str)->list[dict]:
 ts=lex(src);segments=[];current=[]
 for t in ts:
  if t in '.?!;':
   if not current:raise AzuravelError('Punctuation cannot follow an empty clause.')
   segments.append((current,t));current=[]
  else:current.append(t)
 if current:raise AzuravelError('AZ1 requires clause-final punctuation (. ? ! or ;).')
 out=[]
 for body,punct in segments:
  if body[0]=='se':
   if body.count('se')!=1 or body.count('si')!=1:raise AzuravelError('AZ1 permits one non-nested se...si conditional.')
   split=body.index('si')
   a=parse_simple(body[1:split]);b=parse_simple(body[split+1:])
   if a['question'] or a['imperative']:raise AzuravelError('Conditional antecedent must be a declarative, not a question/command.')
   node={'type':'conditional','if':a,'then':b}
   question=b['question'];imp=b['imperative']
  else:
   node=parse_simple(body);question=node['question'];imp=node['imperative']
  if punct=='?' and not question:raise AzuravelError('Question mark requires clause-final ri.')
  if punct=='!' and not imp:raise AzuravelError('Exclamation point in AZ1 is reserved for va commands.')
  if punct in ('.',';') and question:raise AzuravelError('Question ending ri must be followed by ?.')
  node['punctuation']=punct;out.append(node)
 return out

def english_mini(text:str)->str:
 """Small documented subset: <pronoun> [(will|did)] [(not|may|certainly)] <verb>.
    For unaliased concepts: <pronoun> manifest <lexical concept>.
    Also: <pronoun> am/is/are <lexical concept>. Unknown content raises an error.
 """
 text=text.lower().strip().rstrip('.!?')
 m=re.fullmatch(r'(i|you|we|they|they-singular)\s+(?:(will|did)\s+)?(?:(not|may|certainly)\s+)?([a-z]+(?: [a-z]+)?)',text)
 if not m:raise AzuravelError('Supported: I/you/we/they [will|did] [not|may|certainly] <known verb>; or manifest <known concept>.')
 who,tense,modal,verb=m.groups();p={'i':'ya','you':'yu','we':'yi','they':'yo','they-singular':'ye'}[who]
 if verb.startswith('manifest '):
  key=verb[len('manifest '):]
 else:
  matches=[e for e in ENTRIES if e.get('verb_alias')==verb]
  if len(matches)!=1:raise AzuravelError(f'English verb {verb!r} is not mapped. Inspect the dictionary or use manifest <concept>.')
  key=matches[0]['concept']
 entries=[e for e in ENTRIES if e['concept']==key]
 if len(entries)!=1:raise AzuravelError('Unknown concept: '+key)
 words=['ta',p]
 if tense:words.append({'will':'mu','did':'mi'}[tense])
 if modal:words.append({'not':'sa','may':'pa','certainly':'pe'}[modal])
 words.append(entries[0]['forms'][1]['word'])
 result=' '.join(words)+'.';parse_sentence(result)
 return result

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('action',choices=['inspect','encode','decode','parse','english','bits','roundtrip'])
 ap.add_argument('text')
 args=ap.parse_args()
 try:
  fun={'inspect':inspect_word,'encode':payload,'decode':decode_payload,'parse':parse_sentence,'english':english_mini,'bits':barcode_bits,'roundtrip':lambda x:decode_payload(decode_barcode_bits(barcode_bits(payload(x))))}[args.action]
  result=fun(args.text)
  print(json.dumps(result,ensure_ascii=False,indent=2) if isinstance(result,(dict,list)) else result)
 except AzuravelError as exc:
  ap.exit(2,'AZURAVEL invalid: '+str(exc)+'\n')
