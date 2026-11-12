(()=>{'use strict';
const $=id=>document.getElementById(id);
const DATA=JSON.parse($('az-data').textContent);
const ENTRIES=DATA.entries;
const STAR_SOURCE=JSON.parse($('starsilk-data').textContent);
const STAR_RECORDS=STAR_SOURCE.cases;
// A reading sequence assembled only from the four source-bound testimonies.
// It is NOT a shared historical chronology, casualty calculation, or literal map.
const LEDGER=[
 {name:'THE FILE',title:'It worked.',lead:'Four operations can be entered in a ledger as successful.',sub:'The Blood Rings were mapped. The Siege Wall held. The Pyric titan fell. A refugee survived to call these outcomes salvation. These are separate source records, not one operation or a proven causal chain. Their official descriptions need not mention what they consumed.',source:'COMPARATIVE READING / FOUR AUTHORIAL TESTIMONIES / NOT AZ1'},
 {name:'THE COST',title:'What the reports cannot subtract.',lead:'The results remain true. The losses were true at the same time.',sub:'Civilizations were homogenized into orbital material. Inhabited suns were collapsed into a black-hole lattice. Nacreous VI survived as a Level 3 remnant. Codec himself chose, verified and executed a devastating solution. No illustrated mark denotes one victim, star, distance or coordinate.',source:'SOURCE-BOUND COMPARISON / INTERPRETIVE, NOT TO SCALE'},
 {name:'THE CUP',title:'Necessary is not saved.',lead:'One red reflection on a dented cup. Nothing else has to move.',sub:'The reflection is a heater light, not another Blood Ring. Codec watches it after recalling his maps, Tiger’s containment and his own strike. “I became necessary. That is not the same thing.” Tactical effectiveness did not turn these choices into innocence.',source:'CODEC TESTIMONY / FINAL AUTHORIAL READING / NOT AZ1'}
];
const BY_ID=new Map(ENTRIES.map(e=>[e.id,e]));
const DOMAINS=[...new Set(ENTRIES.map(e=>e.domain))];
const ROLES=['CONC','EVT','SRC','PAT','RES','CTR'];
const RULES={CONC:'The concept or instance.',EVT:'The occurrence: something manifests.',SRC:'The agent or source from which it comes.',PAT:'The bearer or recipient affected.',RES:'The trace or result it leaves.',CTR:'An active counter-event. Not a simple negation.'};
const RECORDS=[
 {key:'WITNESS / 01',title:'The census of names',entry:'I03',linked:['I02','I06'],short:'First they counted names. Then they counted bodies. The two lists agreed until the memories were counted.',long:'That disagreement is the entire surviving record. The grammar can say what a name is, who bears it, what remains after it is spoken, and that it was actively suppressed. It cannot identify the missing person.',question:'If a name is counteracted, who remains to answer it?',unlock:'Available from the first observation.'},
 {key:'WITNESS / 02',title:'The boundary that returned',entry:'I09',linked:['S08','M10'],short:'They named it a doorway. They approached. They crossed. When they returned, the boundary had the same position, but their testimony did not.',long:'In this reconstruction the route remains physically traceable. What changes is the grammar of the crossing: an event and its counter-event are independent claims. A return is not proof that a crossing never occurred.',question:'What kind of structure can cancel an action without moving its threshold?',unlock:'Inspect at least one registered root.'},
 {key:'WITNESS / 03',title:'An event with no sound',entry:'I05',linked:['I06','E03'],short:'The first transcript is empty. The second is not. It records the deliberate suppression of a voice. Those cannot be the same statement.',long:'AZ1 refuses to collapse a negated manifestation into a counter-event. “It did not happen” and “something prevented or reversed it” have different forms. The distinction may be the only evidence that an action took place.',question:'When does silence become evidence of a silencing?',unlock:'Find the active counter-event form of any root.'},
 {key:'WITNESS / 04',title:'The residue of a promise',entry:'R06',linked:['E09','L04'],short:'Someone made a promise. Someone did not keep it. What remained was neither the promise nor the act that ended it.',long:'The result state has its own grammatical form. So does the counter-event. This does not prove that traces survive in the physical world. It means that the language leaves a place for them in a description, even when the event has ended.',question:'What survives in an archive when the thing it names no longer does?',unlock:'Investigate three distinct roots.'},
 {key:'WITNESS / 05',title:'The second person',entry:'I01',linked:['I02','K09'],short:'The final record contains an address: you. Not a discovered identity. A grammatical position, waiting long before anyone occupied it.',long:'The AZ1 particle yu marks second-person singular. This instrument does not know who you are. It can still display a sentence that has a place for an addressee. A place in a grammar is not proof of a witness—but the difference can feel thin.',question:'If a sentence has a position for you, who was it written to reach?',unlock:'Inspect four roots and four grammatical roles.'}
];
const HOST=$('observatory'),NODES=$('field-nodes'),FILM=$('ribbon-film'),CANVAS=$('strata-canvas'),CTX=CANVAS.getContext('2d',{alpha:true});
const STORAGE='azuravel.unwitnessed.v1';
const REDUCED=matchMedia('(prefers-reduced-motion: reduce)');
const session={phase:'threshold',domain:null,id:'I01',state:'00',caseIndex:0,visited:new Set(),roles:new Set(),counter:false,motionStopped:false,sound:false,reveal:false,witnessIndex:0,witnessLens:'claim',witnessSeen:new Set(),witnessReturn:null,ledgerStage:0};
let soundCtx=null,soundNodes=[],clock=0,width=0,height=0,dpr=1;
function report(message){$('event-announcer').textContent=message;}
function saved(){try{const s=JSON.parse(localStorage.getItem(STORAGE)||'null');return s&&typeof s==='object'?s:null;}catch{return null;}}
function store(){try{localStorage.setItem(STORAGE,JSON.stringify({visited:[...session.visited],roles:[...session.roles],counter:session.counter,seen:session.reveal,witnessSeen:[...session.witnessSeen]}));}catch{/* Persistence is optional. */}}
function loadProgress(){const s=saved();if(!s)return;
 // A stale or malformed localStorage value is data, not a trusted iterable.
 for(const id of Array.isArray(s.visited)?s.visited.slice(0,100):[])if(typeof id==='string'&&BY_ID.has(id))session.visited.add(id);
 for(const r of Array.isArray(s.roles)?s.roles.slice(0,6):[])if(ROLES.includes(r))session.roles.add(r);
 session.counter=s.counter===true;session.reveal=s.seen===true;
 for(const id of Array.isArray(s.witnessSeen)?s.witnessSeen.slice(0,4):[])if(typeof id==='string'&&STAR_RECORDS.some(r=>r.id===id))session.witnessSeen.add(id);
}
function recordAvailable(){if(session.visited.size<1)return 1;if(!session.counter)return 2;if(session.visited.size<3)return 3;if(session.visited.size<4||session.roles.size<4)return 4;return 5;}
function roleForm(entry,code){return entry.forms.find(f=>f.state===code)||entry.forms[0];}
function entry(){return BY_ID.get(session.id)||ENTRIES[0];}
function writeHash(){if(session.phase==='threshold')return;let route=session.phase==='forms'||session.phase==='differential'?'root='+session.id+'&state='+session.state:session.phase==='roots'?'domain='+encodeURIComponent(session.domain):session.phase==='records'?'record='+session.caseIndex:session.phase==='witness'?'witness='+STAR_RECORDS[session.witnessIndex].id+'&lens='+session.witnessLens:session.phase==='ledger'?'ledger='+session.ledgerStage:'index';if(location.hash!=='#'+route){try{history.replaceState(null,'','#'+route);}catch{}}}
function readHash(){const v=new URLSearchParams(location.hash.replace(/^#/,''));const root=v.get('root'),code=v.get('state'),domain=v.get('domain'),rec=v.get('record'),wit=v.get('witness'),lens=v.get('lens'),ledger=v.get('ledger');if(ledger!==null&&/^[012]$/.test(ledger)){session.ledgerStage=Number(ledger);session.phase='ledger';session.reveal=true;return true;}if(wit){const i=STAR_RECORDS.findIndex(r=>r.id===wit);if(i>=0){session.witnessIndex=i;session.witnessLens=lens==='cost'?'cost':'claim';session.phase='witness';session.reveal=true;return true;}}if(root&&BY_ID.has(root)){session.id=root;session.domain=BY_ID.get(root).domain;session.state=roleForm(entry(),code).state;session.phase='forms';session.reveal=true;return true;}if(domain&&DOMAINS.includes(domain)){session.domain=domain;session.phase='roots';session.reveal=true;return true;}if(rec!==null&&/^\d+$/.test(rec)){session.caseIndex=Math.min(recordAvailable()-1,+rec);session.phase='records';session.reveal=true;return true;}if(location.hash==='#index'){session.phase='sectors';session.reveal=true;return true;}return false;}
function scene(phase){session.phase=phase;session.reveal=true;HOST.dataset.phase=phase;HOST.dataset.ledgerStage=String(session.ledgerStage);$('threshold').hidden=phase!=='threshold';$('field').hidden=phase==='threshold';$('differential').hidden=phase!=='differential';$('connection-status').textContent=phase==='threshold'?'UNSEALED / LOCAL RECONSTRUCTION':(phase==='witness'||phase==='ledger')?'STARSILK / AUTHORIAL READING':'AZ1 / RECONSTRUCTION ACTIVE';writeHash();paint();}
function start(){session.phase='sectors';scene('sectors');report('Boundary crossed. One hundred lexical roots are represented by ten sectors. Select a sector.');}
function goSectors(){session.domain=null;scene('sectors');report('Returned to the outer index.');}
function goRoots(d){if(!DOMAINS.includes(d))return;session.domain=d;scene('roots');report(d+' sector. Ten registered lexical roots available.');}
function goForms(id,code='00'){if(!BY_ID.has(id))return;const e=BY_ID.get(id);session.id=id;session.domain=e.domain;session.state=roleForm(e,code).state;session.visited.add(id);session.roles.add(roleForm(e,code).role);store();scene('forms');report(e.concept+', '+roleForm(e,session.state).role+'.');}
function changeForm(code){const f=roleForm(entry(),code);session.state=f.state;session.roles.add(f.role);if(f.role==='CTR')session.counter=true;store();scene('forms');report(f.word+' is the '+f.role+' state: '+f.meaning+'.');}
function goDifferential(){if(!BY_ID.has(session.id))session.id='I01';scene('differential');report('Contrast: negation states an event does not occur. A counter-event states that suppression or reversal occurs.');}
function goWitness(which=0,lens='claim'){const i=typeof which==='number'?which:STAR_RECORDS.findIndex(r=>r.id===which);if(i<0||i>=STAR_RECORDS.length)return;session.witnessIndex=i;session.witnessLens=lens==='cost'?'cost':'claim';if(session.witnessLens==='cost')session.witnessSeen.add(STAR_RECORDS[i].id);store();scene('witness');report('Source-bound Starsilk testimony: '+STAR_RECORDS[i].title+'. '+(session.witnessLens==='cost'?'Consequences opened.':'Claim opened.'));}
function witnessLens(lens){goWitness(session.witnessIndex,lens);}
function goLedger(stage=0,fromShare=false){
 if(!fromShare&&session.witnessSeen.size!==STAR_RECORDS.length){report('The ledger is incomplete. Examine all four costs first.');return;}
 const n=Number(stage);if(!Number.isInteger(n)||n<0||n>=LEDGER.length)return;
 session.ledgerStage=n;scene('ledger');report('Unclosed Ledger, '+LEDGER[n].name+'. '+LEDGER[n].lead);
}
function goRecord(index=0){if(index<0||index>=recordAvailable())index=0;session.caseIndex=index;scene('records');report('Interpretive case file '+(index+1)+', '+RECORDS[index].title+'.');}
function el(tag,cls,text){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n;}
function action(text,fn,kind=''){const b=el('button',kind?kind+'-action':'',text);b.type='button';b.addEventListener('click',fn);$('reader-actions').append(b);return b;}
function anchor(text,url,kind=''){const b=el('a',kind?kind+'-action':'',text);b.href=url;$('reader-actions').append(b);return b;}
function copyCoordinates(){const link=location.href;if(navigator.clipboard?.writeText){navigator.clipboard.writeText(link).then(()=>report('Coordinates copied to clipboard.'),()=>report('Clipboard unavailable; address bar contains coordinates.'));}else report('Address bar contains these coordinates.');}
function reader({key,kind,title,lead,sub='',source=''}){$('reader-index').textContent=key;$('reader-kind').textContent=kind;$('reader-title').textContent=title;$('reader-lead').textContent=lead;$('reader-sub').textContent=sub;$('reader-source').textContent=source;$('reader-actions').replaceChildren();$('reader-transcript').scrollTop=0;}
function updateReader(){const e=entry(),f=roleForm(e,session.state);if(session.phase==='sectors'){
 reader({key:'INDEX / 000',kind:'100 ROOTS / 600 FORMS',title:'The outer index',lead:'Not stars. One hundred recoverable lexical identities, each represented by six possible grammatical states.',sub:'Choose a region of meaning. Ten sectors contain ten roots each. Every mark can be traced back to an exact registered word.',source:'SOURCE / AZURAVEL_DATA.json • AZ1'});
 action('Begin with identity',()=>goRoots('Identity'),'primary');action('Read the records',()=>goRecord(0));
}else if(session.phase==='roots'){
 const group=ENTRIES.filter(x=>x.domain===session.domain);
 reader({key:'SECTOR / '+String(DOMAINS.indexOf(session.domain)+1).padStart(2,'0'),kind:'10 ROOTS / 60 STATES',title:session.domain,lead:'Every visible label is one canonical root. The rest of its six states are present but not yet exposed.',sub:'Choose a word. The same three syllables will identify its concept, its occurrence, its source, its recipient, its result, and its active counteraction.',source:group.map(x=>x.root).join(' · ')});
 action('Inspect '+group[0].root,()=>goForms(group[0].id),'primary');action('Outer index',goSectors);
}else if(session.phase==='forms'){
 const note=f.role==='CTR'?'The language does not confuse “did not occur” with “was made to stop.” A counter-event is a positive claim about suppression or reversal.':f.role==='RES'?'A result has its own form. Its existence is not guaranteed by the grammar; the grammar gives a trace a place to be described.':f.role==='PAT'?'The same lexical identity can name the bearer of an action. What was abstract has acquired a recipient.':f.role==='SRC'?'The syntax can assign a source to the same concept. The shape changes; the lexical identity does not.':f.role==='EVT'?'A concept is no longer only an object of thought. The event-state asserts that it manifests.':'This is the concept before its five other roles are distinguished.';
 reader({key:'SIGNAL / '+e.id,kind:'AZ1 / '+f.role,title:e.concept,lead:f.word+' — '+f.meaning+'.',sub:note,source:e.example.az+' / '+e.example.en});
 if(f.role==='CTR'){action('See the difference',goDifferential,'primary');action('Evidence files',()=>goRecord(Math.min(2,recordAvailable()-1)));}
 if(f.role!=='CTR')action('Counter-event',()=>changeForm('12'),'primary');
 if(f.role==='RES')action('Compare with counteraction',()=>changeForm('12'));
 action('Other roots',()=>goRoots(e.domain));if(session.witnessReturn)action('Return to testimony',()=>goWitness(session.witnessReturn));anchor('Complete AZ1 lab ↗','./AZURAVEL_ATLAS.html#lab/'+e.id+'/'+f.state);
}else if(session.phase==='witness'){
 const w=STAR_RECORDS[session.witnessIndex],display=w[session.witnessLens],analogy=BY_ID.get(w.root_id);
 reader({key:w.seal,kind:'STARSILK / '+(session.witnessLens==='cost'?'COST':'CLAIM'),title:w.title,lead:display.lead,sub:'Source line: '+w.primary_evidence+' '+display.detail+' '+(session.witnessLens==='cost'?w.question:''),source:'CODEC TESTIMONY / SOURCE-BOUND / NOT AZ1'});
 if(session.witnessLens==='claim')action('Examine the cost',()=>witnessLens('cost'),'primary');
 else action('Revisit the claim',()=>witnessLens('claim'),'primary');
 if(session.witnessIndex<STAR_RECORDS.length-1)action('Next testimony',()=>goWitness(session.witnessIndex+1));
 action('Trace '+analogy.concept+' in AZ1',()=>{session.witnessReturn=w.id;goForms(analogy.id);});
 if(session.witnessSeen.size===STAR_RECORDS.length)action('Assemble the unclosed ledger',()=>goLedger(0),'primary');
 anchor('Source boundary','./STARSILK_SOURCE_BOUNDARY.md');
}else if(session.phase==='ledger'){
 const l=LEDGER[session.ledgerStage];
 reader({key:'UNCLOSED LEDGER / '+String(session.ledgerStage+1).padStart(2,'0')+' OF 03',kind:'STARSILK / SOURCE-BOUND READING',title:l.title,lead:l.lead,sub:l.sub,source:l.source});
 if(session.ledgerStage<2)action(session.ledgerStage===0?'Expose the cost':'Go to the cup',()=>goLedger(session.ledgerStage+1),'primary');
 else action('Return to the four',()=>goLedger(0),'primary');
 action('Revisit Codec’s account',()=>goWitness(3,'cost'));
 anchor('Source boundary','./STARSILK_SOURCE_BOUNDARY.md');
}else if(session.phase==='differential'){
 reader({key:'CONTRAST / AZ1',kind:'MORPHOLOGY / VERIFIED',title:'This is not nothing.',lead:'An absence and an act of erasure are different observations.',sub:'sa + EVT negates an occurrence. CTR is its own predicate: suppression, reversal or counteraction actually takes place. The distinction is part of AZ1, not a claim that any historical event occurred.',source:'AZ1 SPECIFICATION / §3 • NEGATION ≠ COUNTER-EVENT'});
 action('Return to six states',()=>scene('forms'),'primary');action('A case of silence',()=>goRecord(Math.min(2,recordAvailable()-1)));anchor('Read the rule ↗','./AZURAVEL_SPEC.md');
}else if(session.phase==='records'){
 const r=RECORDS[session.caseIndex],root=BY_ID.get(r.entry);
 reader({key:r.key,kind:'SPECULATIVE / NOT CANON',title:r.title,lead:r.short,sub:r.long+' '+r.question,source:root.example.az+' / '+root.example.en});
 if(session.caseIndex<recordAvailable()-1)action('Next fragment',()=>goRecord(session.caseIndex+1),'primary');
 else if(session.caseIndex<RECORDS.length-1)action('Unlock: explore the index',()=>goForms(r.entry),'primary');
 action('Trace '+root.root,()=>goForms(root.id));action('The outer index',goSectors);
}
 $('field-coordinate').textContent=session.phase==='forms'?'[ '+e.id+' / '+f.state+' / '+f.role+' ]':session.phase==='records'?'[ FIELD NOTE '+String(session.caseIndex+1).padStart(2,'0')+' / '+RECORDS.length+' ]':session.phase==='witness'?'[ STAR SILK / '+(session.witnessIndex+1)+' OF '+STAR_RECORDS.length+' ]':session.phase==='ledger'?'[ UNCLOSED LEDGER / '+(session.ledgerStage+1)+' OF 3 ]':'[ INDEX / '+(session.domain||'ALL SECTORS').toUpperCase()+' ]';
 $('discovery-count').textContent=session.phase==='ledger'?'4 SOURCE RECORDS / NO CASUALTY TOTAL':session.phase==='witness'?session.witnessSeen.size+' / 4 COST READINGS':session.visited.size+' / 100 INVESTIGATED';
 $('rail-index').setAttribute('aria-current',session.phase==='sectors'||session.phase==='roots'||session.phase==='forms'?'true':'false');
 $('rail-records').setAttribute('aria-current',session.phase==='records'?'true':'false');
 $('rail-contrast').setAttribute('aria-current',session.phase==='differential'?'true':'false');
 $('rail-witness').setAttribute('aria-current',(session.phase==='witness'||session.phase==='ledger')?'true':'false');
}
function point(i,n,mode){if(innerWidth<761&&mode==='record')return{x:[23,50,77][i],y:18};if(innerWidth<761){const col=mode==='form'?i%3:i%5;const row=mode==='form'?Math.floor(i/3):Math.floor(i/5);const x=mode==='form'?[21,50,79][col]:[13,31.5,50,68.5,87][col];return{x,y:row?52:16};}
 const angle=-Math.PI/2+(i/n)*Math.PI*2;const rx=mode==='form'?30:31,ry=mode==='form'?27:25;return{x:54+rx*Math.cos(angle),y:33+ry*Math.sin(angle)};
}
function node({title,sub='',count='',current=false,x,y,kind,click}){const b=el('button','glyph-node');b.type='button';b.dataset.kind=kind;b.style.setProperty('--x',x);b.style.setProperty('--y',y);b.setAttribute('aria-current',current?'true':'false');b.setAttribute('aria-label',[title,sub,count].filter(Boolean).join(', '));b.append(el('span','node-title',title));if(sub)b.append(el('span','node-sub',sub));if(count)b.append(el('span','node-count',count));b.addEventListener('click',click);NODES.append(b);}
function updateNodes(){NODES.replaceChildren();const phase=session.phase;
 if(phase==='sectors')DOMAINS.forEach((domain,i)=>{const p=point(i,DOMAINS.length,'domain');node({title:domain,sub:'TEN ROOTS',count:String(i+1).padStart(2,'0'),...p,kind:'domain',click:()=>goRoots(domain)});});
 if(phase==='roots')ENTRIES.filter(e=>e.domain===session.domain).forEach((e,i)=>{const p=point(i,10,'root');node({title:e.root,sub:e.concept,count:e.id,...p,kind:'root',click:()=>goForms(e.id)});});
 if(phase==='forms')entry().forms.forEach((f,i)=>{const p=point(i,6,'form');node({title:f.role,sub:f.word,count:f.state,current:f.state===session.state,...p,kind:'form',click:()=>changeForm(f.state)});});
 if(phase==='ledger')LEDGER.forEach((l,i)=>{const x=innerWidth<761?[20,50,80][i]:[37,59,81][i];node({title:l.name,sub:i===0?'CLASSIFICATION':i===1?'CONSEQUENCE':'TESTIMONY',count:String(i+1).padStart(2,'0'),current:i===session.ledgerStage,x,y:innerWidth<761?15:19,kind:'ledger',click:()=>goLedger(i)});});
 if(phase==='witness')STAR_RECORDS.forEach((w,i)=>{const p=point(i,STAR_RECORDS.length,'witness');node({title:w.short,sub:w.glyph.toUpperCase(),count:String(i+1).padStart(2,'0'),current:i===session.witnessIndex,...p,kind:'witness',click:()=>goWitness(i)});});
 if(phase==='records'){const r=RECORDS[session.caseIndex];[r.entry,...r.linked].forEach((id,i)=>{const e=BY_ID.get(id);const p=point(i,3,'record');node({title:e.concept,sub:e.root,count:e.id,...p,kind:'root',click:()=>goForms(e.id)});});}
}
function updateSceneLabels(){const e=entry(),f=roleForm(e,session.state),phase=session.phase;
 const views={sectors:['THE COMPLETE REGISTER','000 / 100'],roots:[(session.domain||'').toUpperCase()+' / FIELD','010 / 060'],forms:[e.id+' / '+e.domain.toUpperCase(),f.role+' / '+f.state],records:['INTERPRETIVE RECONSTRUCTION','WITNESS / '+String(session.caseIndex+1).padStart(2,'0')],differential:['THE CRITICAL DISTINCTION','NOT AN ABSENCE'],witness:['AUTHORIAL STARSILK TESTIMONY','NOT AZ1 CANON'],ledger:['THE UNCLOSED LEDGER','FOUR READINGS / ONE QUESTION']};
 $('scene-designation').textContent=views[phase]?.[0]||'THE INSTRUMENT';$('scene-number').textContent=views[phase]?.[1]||'';
 $('large-word').textContent=phase==='forms'?f.word:phase==='roots'?session.domain.toLowerCase():phase==='sectors'?'600':phase==='records'?RECORDS[session.caseIndex].key:phase==='witness'?STAR_RECORDS[session.witnessIndex].short:phase==='ledger'?'':'';
 $('large-syllables').replaceChildren();if(phase==='forms')for(let i=0;i<3;i++)$('large-syllables').append(el('span','',f.word.slice(i*2,i*2+2)));
 $('large-subtitle').textContent=phase==='forms'?e.concept.toUpperCase()+' / '+f.role+' / '+f.derivation:phase==='roots'?'TEN ROOTS / SIXTY FORMS':phase==='sectors'?'SIX POSSIBLE STATES FOR EACH OF ONE HUNDRED ROOTS':'';
 const evt=roleForm(e,'01'),ctr=roleForm(e,'12');$('absence-form').textContent='sa '+evt.word;$('counter-form').textContent=ctr.word;
 $('horizon-bottom').textContent=phase==='forms'?'[ '+e.id+' : '+f.role+' : '+f.state+' ]':phase==='differential'?'[ NOT EQUIVALENT ]':(phase==='witness'||phase==='ledger')?'[ INTERPRETIVE SCHEMATIC / NOT TO SCALE ]':'[ NO COORDINATES TRANSMITTED ]';
}
function paint(){if(session.phase!=='threshold'){updateSceneLabels();updateReader();updateNodes();}animateScene();updateMotion();}
function resize(){const rect=CANVAS.getBoundingClientRect();width=Math.max(1,rect.width);height=Math.max(1,rect.height);dpr=Math.min(devicePixelRatio||1,1.75);CANVAS.width=Math.round(width*dpr);CANVAS.height=Math.round(height*dpr);CTX.setTransform(dpr,0,0,dpr,0,0);animateScene();if(session.phase!=='threshold')updateNodes();}
function stroke(points,color,lw=1,glow=0){if(points.length<2)return;CTX.beginPath();CTX.moveTo(points[0][0],points[0][1]);for(let i=1;i<points.length;i++)CTX.lineTo(points[i][0],points[i][1]);CTX.strokeStyle=color;CTX.lineWidth=lw;CTX.shadowColor='#007fff';CTX.shadowBlur=glow;CTX.stroke();CTX.shadowBlur=0;}
function drawRegistry(alpha){const ctx=CTX,w=width,h=height,cx=w*(innerWidth<761?.52:.56),cy=h*.40,rx=w*(innerWidth<761?.42:.31),ry=h*.29;
 for(let orbit=0;orbit<5;orbit++){ctx.beginPath();ctx.ellipse(cx,cy,rx*(.42+orbit*.14),ry*(.42+orbit*.14),0,0,Math.PI*2);ctx.strokeStyle='rgba(71,166,232,'+(.055+alpha*.01)+')';ctx.lineWidth=1;ctx.stroke();}
 for(let i=0;i<ENTRIES.length;i++){const sector=Math.floor(i/10),slot=i%10,ang=(sector/10)*Math.PI*2-Math.PI/2,ra=.49+slot*.047;const x=cx+Math.cos(ang)*rx*ra,y=cy+Math.sin(ang)*ry*ra;const active=session.phase==='roots'&&ENTRIES[i].domain===session.domain;const touch=session.phase==='forms'&&ENTRIES[i].id===session.id;
 for(let state=0;state<6;state++){const shift=state*3.1+slot*.32;const xx=x+Math.cos(ang+Math.PI/2)*shift,yy=y+Math.sin(ang+Math.PI/2)*shift;const len=3+state%3*2;stroke([[xx-Math.cos(ang)*len,yy-Math.sin(ang)*len],[xx+Math.cos(ang)*len,yy+Math.sin(ang)*len]],touch?'rgba(139,220,255,.86)':active?'rgba(48,162,247,.55)':'rgba(25,113,190,'+(.22+alpha*.23)+')',touch?1.25:.8,touch?5:0);}
 if(i%10===0){ctx.beginPath();ctx.arc(x,y,1.8,0,Math.PI*2);ctx.fillStyle='rgba(74,180,247,.6)';ctx.fill();}
 }
}
function drawRibbon(phase,alpha){const ctx=CTX,w=width,h=height;const e=entry(),f=roleForm(e,session.state);let count=phase==='forms'?6:phase==='differential'?2:phase==='records'?3:3;
 const centre=w*(innerWidth<761?.5:.62);for(let s=0;s<count;s++){
  const x0=phase==='differential'?w*(s===0?.37:.71):centre+(s-(count-1)/2)*Math.min(w*.14,176);
  const active=phase==='forms'?f.state===e.forms[s]?.state:true;
  const seg=phase==='threshold'?55:phase==='forms'?48:40;
  const points=[];for(let j=0;j<=seg;j++){const t=j/seg,y=h*(.13+.66*t);const wave=Math.sin(t*Math.PI*2*(1.14+s*.11)+(s*1.7))*w*.032;let x=x0+wave;
   if(phase==='differential'&&s===1)x+=(1-t)*w*.04;if(phase==='records')x+=Math.sin(t*7+s*2)*w*.025;
   if(phase==='forms'){const syll=f.word.slice((j%3)*2,(j%3)*2+2);const n=syll.charCodeAt(0);x+=Math.sin(t*9+n*.12)*w*.008;}
   points.push([x,y]);}
  stroke(points,active?'rgba(0,119,245,'+(.11+alpha*.22)+')':'rgba(55,121,196,.08)',active?1.1:.6,active?7:0);
  for(let j=0;j<seg;j++){const t=j/seg,point=points[j];if(phase==='differential'&&s===0&&j>12&&j<29)continue;const len=(active?9:4)+(j%7)*.65;const dx=(j%2?1:-1)*Math.min(9,w*.008);stroke([[point[0]-len+dx,point[1]],[point[0]+len+dx,point[1]]],active?'rgba(66,187,255,'+(.18+alpha*.58)+')':'rgba(47,117,180,.16)',j%9===0?2:1,active&&j%5===0?7:0);}
 }
}

function drawWitness(alpha){
 const ctx=CTX,w=width,h=height,i=session.witnessIndex,cost=session.witnessLens==='cost';
 const cx=w*(innerWidth<761?.51:.60),cy=h*(innerWidth<761?.43:.43),R=Math.min(w*.24,h*.265),lit='rgba(66,184,255,'+(.28+.43*alpha)+')';
 ctx.save();ctx.lineWidth=1.1;ctx.strokeStyle=lit;ctx.shadowBlur=0;
 if(i===0){
   // Blood Ring: orphaned orbital material; deliberately no cartoon halo.
   ctx.beginPath();ctx.ellipse(cx,cy,R*1.45,R*.44,-.17,0,Math.PI*2);ctx.strokeStyle=cost?'rgba(182,79,83,.7)':lit;ctx.stroke();
   ctx.beginPath();ctx.ellipse(cx,cy,R*.67,R*.67,0,0,Math.PI*2);ctx.strokeStyle='rgba(43,110,145,.35)';ctx.stroke();
   for(let j=0;j<92;j++){const t=j*2*Math.PI/92,x=cx+Math.cos(t)*R*1.45,y=cy+Math.sin(t)*R*.44;
     const size=(j%11===0?4:1.4);stroke([[x-size,y],[x+size,y]],cost?'rgba(194,101,100,.72)':'rgba(89,187,240,.48)',j%7===0?1.3:.7);}
 }else if(i===1){
   // Sampled star marks, not a casualty count or actual Siege Wall map.
   ctx.beginPath();ctx.arc(cx,cy,R*.79,0,Math.PI*2);ctx.strokeStyle='rgba(61,132,171,.21)';ctx.stroke();
   for(let j=0;j<56;j++){const t=j*2*Math.PI/56,x=cx+Math.cos(t)*R*(.82+(j%3)*.1),y=cy+Math.sin(t)*R*(.82+(j%5)*.09);
     if(cost){ctx.beginPath();ctx.arc(x,y,1.9+(j%3),0,Math.PI*2);ctx.fillStyle='#020509';ctx.fill();ctx.strokeStyle='rgba(67,145,203,.4)';ctx.stroke();}
     else{stroke([[x-2,y],[x+2,y]],'rgba(99,187,234,.79)',1.1);stroke([[x,y-2],[x,y+2]],'rgba(99,187,234,.79)',1.1);}
   }
   stroke([[cx-R*1.45,cy+R*.36],[cx+R*1.45,cy-R*.36]],'rgba(34,107,167,.36)',1);
 }else if(i===2){
   ctx.beginPath();ctx.arc(cx,cy,R*.86,0,Math.PI*2);ctx.strokeStyle=lit;ctx.stroke();
   if(cost){stroke([[cx-R*.55,cy-R*.49],[cx-R*.16,cy-R*.12],[cx+R*.08,cy+R*.22],[cx+R*.57,cy+R*.49]],'rgba(195,93,91,.74)',2,5);
     stroke([[cx+R*.05,cy+R*.2],[cx-R*.29,cy+R*.49]],'rgba(195,93,91,.54)',1);}
   for(let k=-2;k<=2;k++)stroke([[cx-R*.7,cy+k*R*.24],[cx+R*.7,cy+(k+1)*R*.18]],'rgba(82,154,203,'+(cost?.25:.14)+')',1);
 }else{
   // The source's red reflection on the cup, not a literal Blood Ring.
   ctx.beginPath();ctx.ellipse(cx,cy-R*.40,R*.36,R*.11,0,0,Math.PI*2);ctx.strokeStyle=cost?'rgba(186,79,76,.85)':'rgba(125,159,180,.5)';ctx.lineWidth=cost?2:1;ctx.stroke();
   ctx.beginPath();ctx.moveTo(cx-R*.36,cy-R*.40);ctx.lineTo(cx-R*.26,cy+R*.37);ctx.quadraticCurveTo(cx,cy+R*.6,cx+R*.26,cy+R*.37);ctx.lineTo(cx+R*.36,cy-R*.40);ctx.strokeStyle='rgba(102,168,201,.65)';ctx.stroke();
   ctx.beginPath();ctx.ellipse(cx+R*.38,cy-R*.02,R*.20,R*.29,-.4,-1.25,1.25);ctx.stroke();
   stroke([[cx-R*.27,cy+R*.35],[cx+R*.27,cy+R*.35]],'rgba(99,162,198,.28)',1);
 }
 ctx.restore();
}

function drawLedger(alpha){
 const c=CTX,w=width,h=height,stage=session.ledgerStage,mobile=innerWidth<761;
 c.save();c.lineWidth=1;
 if(stage<2){
  // Four editorial evidence marks, not stars, victims, measured locations or shared historical sites.
  for(let i=0;i<4;i++){
   const x=mobile?w*(i%2?.69:.34):w*(.34+i*.155);
   const y=mobile?h*(i<2?.34:.53):h*.41;
   const R=Math.min(mobile?w*.065:w*.055,h*.115);
   const dark=stage===1,blue='rgba(86,172,232,'+(.30+.45*alpha)+')',red='rgba(190,75,86,'+(.28+.52*alpha)+')';
   c.strokeStyle=dark?red:blue;c.beginPath();c.arc(x,y,R,0,2*Math.PI);c.stroke();
   if(i===0){c.beginPath();c.ellipse(x,y,R*1.50,R*.36,-.24,0,2*Math.PI);c.stroke();if(dark){for(let j=0;j<36;j++){let a=j*Math.PI/18;stroke([[x+Math.cos(a)*R*1.5,y+Math.sin(a)*R*.36],[x+Math.cos(a)*R*1.5+2,y+Math.sin(a)*R*.36+2]],red,.7);}}}
   if(i===1){for(let j=0;j<12;j++){const a=j*Math.PI/6,xx=x+Math.cos(a)*R*.73,yy=y+Math.sin(a)*R*.73;c.beginPath();c.arc(xx,yy,dark?2.2:1.6,0,2*Math.PI);c.strokeStyle=dark?'rgba(188,78,86,.72)':blue;c.stroke();}}
   if(i===2){stroke([[x-R*.7,y-R*.4],[x-R*.24,y+R*.1],[x+R*.12,y-R*.14],[x+R*.7,y+R*.46]],dark?red:blue,dark?2:1);}
   if(i===3){c.beginPath();c.ellipse(x,y-R*.25,R*.40,R*.12,0,0,Math.PI*2);c.stroke();c.beginPath();c.moveTo(x-R*.38,y-R*.25);c.lineTo(x-R*.25,y+R*.56);c.quadraticCurveTo(x,y+R*.78,x+R*.25,y+R*.56);c.lineTo(x+R*.38,y-R*.25);c.stroke();}
   c.fillStyle=dark?'rgba(226,150,157,.82)':'rgba(161,210,246,.75)';c.font='10px ui-monospace,monospace';c.textAlign='center';c.fillText((dark?['MATERIAL','SINGULARITIES','REMNANT','COMPLICITY']:['THE RING','THE WALL','NACREOUS VI','THE CUP'])[i],x,y+R+21);
  }
  if(!mobile){c.beginPath();c.moveTo(w*.26,h*.71);c.lineTo(w*.86,h*.71);c.strokeStyle=stage===1?'rgba(173,71,83,.25)':'rgba(83,168,227,.25)';c.stroke();}
 }else{
  // At the final scale shift all spatial comparison marks disappear.
  // The cup is a heater-lit object from the authored scene, NOT a Blood Ring.
  const x=w*(mobile?.52:.59),y=h*(mobile?.39:.42),R=Math.min(w*.145,h*.205);
  c.beginPath();c.ellipse(x,y-R*.35,R*.40,R*.13,0,0,Math.PI*2);c.strokeStyle='rgba(172,76,79,'+(.40+.54*alpha)+')';c.lineWidth=2;c.stroke();
  c.beginPath();c.moveTo(x-R*.40,y-R*.35);c.lineTo(x-R*.29,y+R*.45);c.quadraticCurveTo(x,y+R*.67,x+R*.29,y+R*.45);c.lineTo(x+R*.40,y-R*.35);c.strokeStyle='rgba(111,166,200,.76)';c.lineWidth=1.2;c.stroke();
  c.beginPath();c.ellipse(x+R*.43,y+R*.035,R*.20,R*.28,-.25,-1.3,1.25);c.stroke();
  c.fillStyle='rgba(187,214,235,'+(.24+.55*alpha)+')';c.font='11px ui-monospace,monospace';c.textAlign='center';c.fillText('A REFLECTION / NOT ANOTHER RING',x,y+R*.95);
 }
 c.restore();
}
function drawFrame(progress){if(!CTX)return;CTX.clearRect(0,0,width,height);const a=Math.max(0,Math.min(1,progress));if(session.phase==='threshold')drawRibbon('threshold',a);if(session.phase==='sectors'||session.phase==='roots')drawRegistry(a);if(session.phase==='forms'){drawRegistry(.3);drawRibbon('forms',a);}if(session.phase==='differential'){drawRegistry(.12);drawRibbon('differential',a);}if(session.phase==='records'){drawRegistry(.08);drawRibbon('records',a);}if(session.phase==='witness'){drawWitness(a);}if(session.phase==='ledger'){drawLedger(a);} }
function animateScene(){if(clock)cancelAnimationFrame(clock);if(REDUCED.matches||session.motionStopped){drawFrame(1);return;}let start=performance.now();const tick=t=>{drawFrame(Math.min(1,(t-start)/920));if(t-start<920&&document.visibilityState!=='hidden')clock=requestAnimationFrame(tick);else clock=0;};clock=requestAnimationFrame(tick);}
function updateMotion(){const paused=REDUCED.matches||session.motionStopped||document.visibilityState==='hidden';const p=FILM;const toggle=$('motion-toggle');if(paused){p.pause();p.style.display='none';}else{p.style.display='';const r=p.play();if(r&&r.catch)r.catch(()=>{p.style.display='none';});}$('motion-label').textContent=session.motionStopped?'RESUME MOTION':'PAUSE MOTION';toggle.setAttribute('aria-pressed',session.motionStopped?'true':'false');toggle.setAttribute('aria-label',session.motionStopped?'Resume movement':'Pause movement');}
async function toggleSound(){if(session.sound){session.sound=false;for(const n of soundNodes){try{n.stop?.();}catch{}}soundNodes=[];if(soundCtx){try{await soundCtx.close();}catch{}}soundCtx=null;}else{const AC=window.AudioContext||window.webkitAudioContext;if(!AC){report('Audio unavailable on this browser.');return;}try{const a=new AC();const gain=a.createGain();gain.gain.value=.0001;gain.connect(a.destination);const tones=[55,82.41];for(let i=0;i<tones.length;i++){const o=a.createOscillator();o.type='sine';o.frequency.value=tones[i];o.connect(gain);o.start();soundNodes.push(o);}gain.gain.linearRampToValueAtTime(.013,a.currentTime+.8);soundCtx=a;session.sound=true;}catch{session.sound=false;report('Audio could not be started.');}}
 $('sound-label').textContent=session.sound?'SOUND ON':'SOUND OFF';$('sound-toggle').setAttribute('aria-pressed',session.sound?'true':'false');$('sound-toggle').setAttribute('aria-label',session.sound?'Disable quiet ambient audio':'Enable quiet ambient audio');}
function onKey(ev){const tag=document.activeElement?.tagName;if(['INPUT','TEXTAREA','SELECT'].includes(tag))return;if(ev.key==='Escape'&&session.phase!=='threshold'){if(session.phase==='forms')goRoots(entry().domain);else if(session.phase==='roots')goSectors();else if(session.phase==='differential')scene('forms');else if(session.phase==='ledger')goWitness(3,'cost');else goSectors();ev.preventDefault();}else if((ev.key==='ArrowRight'||ev.key==='ArrowLeft')&&session.phase==='forms'&&document.activeElement===document.body){const i=entry().forms.findIndex(x=>x.state===session.state);changeForm(entry().forms[(i+(ev.key==='ArrowRight'?1:5))%6].state);ev.preventDefault();}}
function init(){loadProgress();$('enter-observatory').addEventListener('click',start);$('enter-testimony').addEventListener('click',()=>goWitness(0));$('motion-toggle').addEventListener('click',()=>{session.motionStopped=!session.motionStopped;updateMotion();animateScene();});$('sound-toggle').addEventListener('click',toggleSound);
 for(const b of document.querySelectorAll('[data-route]'))b.addEventListener('click',()=>{const x=b.dataset.route;if(x==='witness')goWitness(session.witnessIndex);else if(x==='records')goRecord(Math.min(session.caseIndex,recordAvailable()-1));else if(x==='differential')goDifferential();else goSectors();});
 document.addEventListener('keydown',onKey);window.addEventListener('resize',resize,{passive:true});document.addEventListener('visibilitychange',()=>{updateMotion();if(soundCtx){if(document.hidden)soundCtx.suspend();else if(session.sound)soundCtx.resume();}if(!document.hidden)animateScene();});
 const onReduce=()=>{updateMotion();animateScene();};if(REDUCED.addEventListener)REDUCED.addEventListener('change',onReduce);else if(REDUCED.addListener)REDUCED.addListener(onReduce);
 window.addEventListener('pagehide',()=>{if(clock)cancelAnimationFrame(clock);FILM.pause();if(soundCtx)soundCtx.close();});
 window.addEventListener('hashchange',()=>{const h=session.phase;if(readHash())scene(session.phase);else if(session.phase!=='threshold')paint();});
 if(readHash())scene(session.phase);else{HOST.dataset.phase='threshold';$('threshold').hidden=false;$('field').hidden=true;}
 resize();updateMotion();report('AZURAVEL observatory loaded. Cross the boundary to explore.');}
// Read-only introspection is used by project regression tests. It cannot edit the lexicon.
window.AZURAVEL_OBSERVATORY_TEST=Object.freeze({snapshot:()=>({phase:session.phase,domain:session.domain,id:session.id,state:session.state,visited:[...session.visited],roles:[...session.roles],availableRecords:recordAvailable(),counter:session.counter,witnessIndex:session.witnessIndex,witnessLens:session.witnessLens,witnessViewed:session.witnessSeen.size,ledgerStage:session.ledgerStage}),enter:start,openDomain:goRoots,openRoot:goForms,openRole:changeForm,openRecord:goRecord,contrast:goDifferential,roleForm:(id,code)=>{const e=BY_ID.get(id);return e?roleForm(e,code):null;},records:()=>RECORDS.map(r=>({key:r.key,entry:r.entry})),nodeCount:()=>NODES.children.length,openWitness:goWitness,openWitnessLens:witnessLens,openLedger:goLedger,source:()=>({protocol:STAR_SOURCE.protocol,records:STAR_RECORDS.map(r=>({id:r.id,root_id:r.root_id,source_scope:r.source_scope}))})});
init();
})();
