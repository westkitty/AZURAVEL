"""AZURAVEL rigorous offline reference tests: named cases, plus exhaustive loops."""
import unittest
from itertools import product
from pathlib import Path
from azuravel_ref import *

class TestAzuravel(unittest.TestCase):
 def assert_bad(self,fn,*args):
  with self.assertRaises(AzuravelError):fn(*args)
 def test_01_root_count(self):self.assertEqual(len(ENTRIES),100)
 def test_02_domain_count(self):self.assertEqual(len({e['domain'] for e in ENTRIES}),10)
 def test_03_ten_roots_per_domain(self):
  for d in set(e['domain'] for e in ENTRIES):self.assertEqual(sum(e['domain']==d for e in ENTRIES),10)
 def test_04_canonical_roots_unique(self):self.assertEqual(len(ROOTS),100)
 def test_05_all_six_forms_unique(self):self.assertEqual(len(FORM),600)
 def test_06_three_distinct_root_consonants(self):
  for e in ENTRIES:self.assertEqual(len({c[0] for c in syllables(e['root'])}),3)
 def test_07_root_order_is_canonical(self):
  for e in ENTRIES:self.assertEqual(canonical(e['root']),e['root'])
 def test_08_every_lexeme_has_six_forms(self):
  for e in ENTRIES:self.assertEqual(len(e['forms']),6)
 def test_09_permutations_exhaustive_and_bijective(self):
  for e in ENTRIES:
   self.assertEqual({transform(e['root'],s,r) for s,r in product([0,1],range(3))},{f['word'] for f in e['forms']})
 def test_10_every_surface_inverse_returns_same_root(self):
  for word,(e,f) in FORM.items():self.assertEqual(canonical(word),e['root'])
 def test_11_normal_form_state_unique(self):
  for e in ENTRIES:
   for f in e['forms']:
    a=inspect_word(f['word']);self.assertEqual(a['state'],f['state']);self.assertEqual(a['id'],e['id'])
 def test_12_stress_per_lexeme(self):
  for e in ENTRIES:
   for f in e['forms']:
    self.assertEqual(f['ipa'].count('ˈ'),1);self.assertNotIn('rr',f['ipa'])
 def test_13_particles_are_closed_class(self):self.assertEqual(len(PARTICLES),26)
 def test_14_all_particles_cv_and_pronounceable(self):
  for p in PARTICLES:self.assertEqual(len(p),2);self.assertIn(p[0],DATA['consonants']);self.assertIn(p[1],VOWELS)
 def test_15_short_word_rejected(self):self.assert_bad(inspect_word,'kemi')
 def test_16_extra_syllable_rejected(self):self.assert_bad(inspect_word,'kemiroka')
 def test_17_invalid_root_consonant_rejected(self):self.assert_bad(inspect_word,'dapomi')
 def test_18_invalid_vowel_rejected(self):self.assert_bad(inspect_word,'kxmira')
 def test_19_duplicate_consonant_rejected(self):self.assert_bad(inspect_word,'kakeli')
 def test_20_uppercase_rejected(self):self.assert_bad(inspect_word,'KeMiRo')
 def test_21_unknown_wellformed_root_rejected(self):
  unknown=next(''.join(cs[i]+v for i,v in enumerate('aaa')) for cs in [('k','l','m'),('k','l','n'),('k','l','r'),('k','l','s'),('k','l','t')] if ''.join(c+'a' for c in cs) not in ROOTS)
  self.assert_bad(inspect_word,unknown)
 def test_22_illegal_swap_parameter(self):self.assert_bad(transform,'kemiro',2,0)
 def test_23_illegal_rotation_parameter(self):self.assert_bad(transform,'kemiro',0,3)
 def test_24_transform_requires_canonical_input(self):self.assert_bad(transform,'miroke',0,1)
 def test_25_all_forms_have_payload(self):
  for word in FORM:self.assertTrue(payload(word).startswith('AZ1|'))
 def test_26_all_payloads_reversible(self):
  for word in FORM:self.assertEqual(decode_payload(payload(word))['surface'],word)
 def test_27_payload_bad_version_rejected(self):self.assert_bad(decode_payload,'AZ2|I01|0|1|miroke')
 def test_28_payload_bad_id_rejected(self):self.assert_bad(decode_payload,'AZ1|Z99|0|1|miroke')
 def test_29_payload_case_rejected(self):self.assert_bad(decode_payload,'AZ1|I01|0|1|MIROKE')
 def test_30_payload_extra_field_rejected(self):self.assert_bad(decode_payload,'AZ1|I01|0|1|miroke|junk')
 def test_31_payload_state_surface_mismatch(self):self.assert_bad(decode_payload,'AZ1|I01|0|0|miroke')
 def test_32_payload_id_surface_mismatch(self):self.assert_bad(decode_payload,'AZ1|I02|0|1|miroke')
 def test_33_code128_has_complete_pattern_table(self):self.assertEqual(len(SYMBOL_PATTERNS),107)
 def test_34_code128_pattern_widths(self):
  for p in SYMBOL_PATTERNS[:106]:self.assertEqual(sum(int(x) for x in p),11);self.assertEqual(len(p),6)
  self.assertEqual(sum(int(x) for x in SYMBOL_PATTERNS[106]),13)
 def test_35_code128_patterns_unique(self):self.assertEqual(len(set(SYMBOL_PATTERNS)),107)
 def test_36_code128_checksum_known_ABC_vector(self):self.assertEqual(code128_symbols('ABC'),[104,33,34,35,1,106])
 def test_37_code128_roundtrip_ABC(self):self.assertEqual(decode_barcode_bits(barcode_bits('ABC')),'ABC')
 def test_38_code128_all_600_payloads_modules(self):
  for word in FORM:
   x=payload(word);self.assertEqual(decode_barcode_bits(barcode_bits(x)),x)
 def test_39_code128_quiet_zones(self):
  b=barcode_bits('ABC');self.assertTrue(b.startswith('0'*10));self.assertTrue(b.endswith('0'*10))
 def test_40_code128_quiet_zones_missing_rejected(self):self.assert_bad(decode_barcode_bits,barcode_bits('ABC')[2:])
 def test_41_code128_stop_corruption_rejected(self):
  b=barcode_bits('ABC');i=len(b)-10-6;self.assert_bad(decode_barcode_bits,b[:i]+('0' if b[i]=='1' else '1')+b[i+1:])
 def test_42_code128_checksum_corruption_rejected(self):
  s=code128_symbols('ABC');s[1]=34
  b='0'*10+''.join(symbol_bits(x) for x in s)+'0'*10
  self.assert_bad(decode_barcode_bits,b)
 def test_43_code128_invalid_char_rejected(self):self.assert_bad(code128_symbols,'hello \u2022')
 def test_44_code128_illegal_switch_rejected(self):
  ss=[104,99,0,0,106];b='0'*10+''.join(symbol_bits(x) for x in ss)+'0'*10
  self.assert_bad(decode_barcode_bits,b)
 def test_45_all_twenty_sentences_parse(self):
  self.assertEqual(len(DATA['sentences']),20)
  for s in DATA['sentences']:self.assertTrue(parse_sentence(s['az']),s['tag'])
 def test_46_all_sentence_ipa_token_count(self):
  for s in DATA['sentences']:
   self.assertEqual(s['ipa'],pronunciation(s['az']))
 def test_47_no_unparsed_sentence_word(self):
  for s in DATA['sentences']:
   for t in lex(s['az']):self.assertTrue(t in FORM or t in PARTICLES or t in '.?!;')
 def test_48_question_requires_ri(self):self.assert_bad(parse_sentence,'ta yu miroke?')
 def test_49_question_ri_requires_question_mark(self):self.assert_bad(parse_sentence,'ta yu miroke ri.')
 def test_50_no_pat_requires_causative(self):self.assert_bad(parse_sentence,'ta ya no kemiro miroke.')
 def test_51_valid_causative(self):self.assertTrue(parse_sentence('ta ya no kemiro ko miroke.'))
 def test_52_verb_used_as_np_rejected(self):self.assert_bad(parse_sentence,'ta miroke miroke.')
 def test_53_noun_used_as_verb_rejected(self):self.assert_bad(parse_sentence,'ta ya kemiro.')
 def test_54_duplicate_actor_rejected(self):self.assert_bad(parse_sentence,'ta ya ta yu miroke.')
 def test_55_feature_order_must_be_canonical(self):self.assert_bad(parse_sentence,'ta ya sa mi miroke.')
 def test_56_singular_reciprocity_rejected(self):self.assert_bad(parse_sentence,'ta ya lo miroke.')
 def test_57_plural_reciprocity_accepted(self):self.assertTrue(parse_sentence('ta yi lo miroke.'))
 def test_58_illegal_la_pronoun(self):self.assert_bad(parse_sentence,'ta la ya miroke.')
 def test_59_legal_la_nominal(self):self.assertTrue(parse_sentence('ta la kemiro miroke.'))
 def test_60_possession_missing_head(self):self.assert_bad(parse_sentence,'ta ya li miroke.')
 def test_61_possession_valid(self):self.assertTrue(parse_sentence('ta ya li kemiro no lomati ra.'))
 def test_62_copula_needs_complement(self):self.assert_bad(parse_sentence,'ta ya ra.')
 def test_63_copula_no_aspect(self):self.assert_bad(parse_sentence,'ta ya no lomati ne ra.')
 def test_64_imperative_valid(self):self.assertTrue(parse_sentence('va miroke!'))
 def test_65_imperative_explicit_subject_rejected(self):self.assert_bad(parse_sentence,'va ta yu miroke!')
 def test_66_conditional_valid(self):self.assertTrue(parse_sentence('se ta ya miroke si ta yu mu miroke.'))
 def test_67_conditional_missing_si(self):self.assert_bad(parse_sentence,'se ta ya miroke ta yu mu miroke.')
 def test_68_conditional_nested_rejected(self):self.assert_bad(parse_sentence,'se ta ya miroke si se ta yu miroke si ta yi miroke.')
 def test_69_english_mini_known_verb(self):self.assertTrue(english_mini('I will travel').startswith('ta ya mu '))
 def test_70_english_mini_unknown_verb_rejected(self):self.assert_bad(english_mini,'I will teleport')
 def test_71_english_mini_no_fake_unknown(self):self.assert_bad(english_mini,'I manifest invented')
 def test_72_english_mini_negation(self):self.assertTrue('sa' in english_mini('I will not travel'))
 def test_73_barcode_svg_true_vector(self):
  a=barcode_svg('ABC');self.assertIn('viewBox=',a);self.assertIn('<rect',a);self.assertIn('fill="black"',a)
 def test_74_palette_identity(self):self.assertEqual(DATA['palette']['azure'],'#007FFF')
 def test_75_barcodes_stay_black_white(self):self.assertNotIn('#007FFF',barcode_svg('ABC'))
 def test_76_glyph_cv_mapping_injective(self):
  consonants=DATA['consonants'];vowels=DATA['vowels'];glyphs={}
  for ci,c in enumerate(consonants):
   for vi,v in enumerate(vowels):
    mapping=(tuple(bool(ci & (1 << b)) for b in range(4)),vi)
    self.assertNotIn(mapping,glyphs)
    glyphs[mapping]=c+v
  self.assertEqual(len(glyphs),55)
 def test_77_no_spider_string_in_generated_content(self):
  # Standing visual/content constraint; not part of lexical grammar itself.
  for s in DATA['sentences']:self.assertNotIn('spider',s['en'].lower())
 def test_79_all_dictionary_example_sentences_are_valid(self):
  for e in ENTRIES:self.assertTrue(parse_sentence(e['example']['az']),e['id'])
 def test_80_all_roots_have_three_or_more_derived_meanings(self):
  for e in ENTRIES:
   self.assertGreaterEqual(len(e['forms'])-1,3)
   for f in e['forms'][1:]:
    self.assertIn(e['concept'],f['meaning']);self.assertTrue(f['derivation'].startswith('S'))
 def test_78_real_optical_scan_independent(self):
  try:
   from pyzbar.pyzbar import decode
   from PIL import Image,ImageDraw
  except ImportError:
   self.skipTest('pyzbar cannot load libzbar')
  examples=['ABC',payload(ENTRIES[0]['forms'][0]['word']),payload(ENTRIES[0]['forms'][1]['word']),payload(ENTRIES[19]['forms'][5]['word']),payload(ENTRIES[-1]['forms'][3]['word'])]
  for txt in examples:
   bits=barcode_bits(txt);x=4;h=160
   im=Image.new('RGB',(len(bits)*x,h),'white');draw=ImageDraw.Draw(im)
   for i,b in enumerate(bits):
    if b=='1':draw.rectangle((i*x,12,(i+1)*x-1,h-12),fill='black')
   decoded=decode(im)
   self.assertTrue(decoded,f'No optical decode of {txt}')
   self.assertEqual(decoded[0].data.decode('ascii'),txt)

if __name__=='__main__':unittest.main(verbosity=2)
