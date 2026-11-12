"""AZURAVEL 1.1 independent browser/API/UI regression checks. Run with: python -m unittest -v test_uplift.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import unittest, hashlib, json, os
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent
HTML=(ROOT/'AZURAVEL_ATLAS.html').read_text()
DATA=json.loads((ROOT/'AZURAVEL_DATA.json').read_text())
PROTECTED=json.loads((ROOT/'PROTECTED_HASHES.json').read_text())

class UpliftRegression(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.playwright=sync_playwright().start()
  cls.browser=cls.playwright.chromium.launch(headless=True, executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 @classmethod
 def tearDownClass(cls):
  cls.browser.close();cls.playwright.stop()
 def setUp(self):
  self.page=self.browser.new_page(viewport={'width':1440,'height':900})
  self.errors=[];self.page.on('pageerror',lambda err:self.errors.append(str(err)))
  self.page.set_content(HTML,wait_until='load')
 def tearDown(self):
  self.assertEqual([],self.errors, 'Uncaught browser JavaScript errors')
  self.page.close()
 def nav(self,name):self.page.locator(f'.nav-item[data-view="{name}"]').click()
 def test_source_semantics_byte_preserved(self):
  for name,expected in PROTECTED.items():
   self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),expected,name)
 def test_embedded_json_matches_normative_data(self):
  actual=self.page.evaluate("JSON.parse(document.getElementById('az-data').textContent)")
  self.assertEqual(DATA,actual)
 def test_six_views_work_without_exceptions(self):
  self.assertEqual(6,self.page.locator('.nav-item').count())
  for view in ['lab','lexicon','syntax','translate','protocol','practice']:
   self.nav(view);self.assertTrue(self.page.locator('#view-'+view).is_visible())
   self.assertEqual(1,self.page.locator('.nav-item[aria-selected="true"]').count())
 def test_all_viewport_widths_six_views(self):
  for width in [320,360,390,768,1024,1440]:
   self.page.set_viewport_size({'width':width,'height':850})
   for view in ['lab','lexicon','syntax','translate','protocol','practice']:
    self.nav(view)
    self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width+1,(width,view))
 def test_keyboard_tabs_roving_and_focus(self):
  a=self.page.locator('.nav-item[data-view="lab"]');a.focus()
  self.page.keyboard.press('ArrowRight')
  self.assertEqual('Root registry',self.page.locator('.nav-item[aria-selected="true"]').inner_text().split('02')[-1].strip())
  self.assertEqual('tab-lexicon',self.page.evaluate('document.activeElement.id'))
  self.page.keyboard.press('End')
  self.assertEqual('tab-practice',self.page.evaluate('document.activeElement.id'))
  self.page.keyboard.press('Home')
  self.assertEqual('tab-lab',self.page.evaluate('document.activeElement.id'))
  self.assertEqual(1,self.page.locator('.nav-item[tabindex="0"]').count())
 def test_loom_shows_three_fixed_syllable_paths(self):
  self.assertEqual(3,self.page.locator('#loom-root .loom-tile').count())
  self.assertEqual(3,self.page.locator('#loom-output .loom-tile').count())
  self.assertEqual(3,self.page.locator('#loom-lines svg path').count())
  self.assertEqual(['ke','mi','ro'],self.page.locator('#loom-root .loom-tile strong').all_inner_texts())
  self.assertEqual(['mi','ro','ke'],self.page.locator('#loom-output .loom-tile strong').all_inner_texts())
 def test_loom_operations_inverse_and_reset(self):
  start=self.page.locator('#selected-word .word').inner_text()
  self.page.locator('#loom-left').click();left=self.page.locator('#selected-word .word').inner_text()
  self.assertNotEqual(start,left)
  self.page.locator('#loom-right').click();self.assertEqual(start,self.page.locator('#selected-word .word').inner_text())
  self.page.locator('#loom-undo').click();self.assertEqual(left,self.page.locator('#selected-word .word').inner_text())
  self.page.locator('#loom-reset').click();self.assertEqual('kemiro',self.page.locator('#selected-word .word').inner_text())
 def test_loom_swap_is_self_inverse(self):
  self.page.locator('#loom-swap').click();self.page.locator('#loom-swap').click()
  self.assertEqual('miroke',self.page.locator('#selected-word .word').inner_text())
 def test_keyboard_loom_shortcut(self):
  self.page.locator('#loom-history').focus();self.page.keyboard.press('s')
  self.assertEqual('romike',self.page.locator('#selected-word .word').inner_text())
  self.page.keyboard.press('u');self.assertEqual('miroke',self.page.locator('#selected-word .word').inner_text())
 def test_loom_reset_after_manual_state_selection(self):
  self.page.locator('#loom-swap').click()
  self.page.locator('#states button[data-state="02"]').click()
  self.assertTrue(self.page.locator('#loom-undo').is_disabled())
  self.assertIn('select an operation',self.page.locator('#loom-history').inner_text())
 def test_loom_reset_after_text_input_changes_state(self):
  self.page.locator('#loom-swap').click()
  self.page.locator('#word-input').fill('miker o'.replace(' ',''))
  self.page.locator('#inspect-btn').click()
  self.assertTrue(self.page.locator('#loom-undo').is_disabled())
 def test_loom_cross_root_changes_reset_history(self):
  self.page.locator('#loom-swap').click()
  self.nav('lexicon');self.page.locator('#root-search').fill('memory')
  self.page.locator('#lex-items button').first.click()
  self.assertTrue(self.page.locator('#loom-undo').is_disabled())
  self.assertEqual('meniro',self.page.locator('#selected-word .word').inner_text())
 def test_handoff_to_sentence_builder(self):
  self.page.locator('#use-as-predicate').click()
  self.assertTrue(self.page.locator('#view-syntax').is_visible())
  self.assertEqual('I01',self.page.locator('#b-concept').input_value())
  self.assertIn('miroke',self.page.locator('#build-output').inner_text())
 def test_handoff_to_decoder_preserves_payload(self):
  self.page.locator('#loom-swap').click()
  payload=self.page.locator('#payload-select').input_value()
  self.page.locator('#verify-in-decoder').click()
  self.assertEqual(payload,self.page.locator('#scan-input').input_value())
  self.assertEqual('false',self.page.locator('#scan-result').get_attribute('data-error'))
 def test_code128_encoding_proof(self):
  self.page.locator('details.codeproof summary').click()
  text=self.page.locator('#codeword-inspector').inner_text()
  self.assertIn('START B',text);self.assertIn('WEIGHTED CHECK',text);self.assertIn('STOP',text);self.assertIn('QUIET ZONES',text)
  self.assertEqual('AZ1|I01|0|1|miroke',self.page.locator('#payload-select').input_value())
 def test_full_registry_integrity_audit(self):
  self.nav('protocol');self.page.locator('#audit-run').click()
  self.assertEqual('false',self.page.locator('#audit-summary').get_attribute('data-error'))
  self.assertIn('600 forms checked',self.page.locator('#audit-summary').inner_text())
  self.assertEqual(600,self.page.locator('#audit-grid i.pass').count())
 def test_permutation_group_algebra_for_all_600_forms(self):
  result=self.page.evaluate('''()=>{const T=window.AZURAVEL_TEST;const D=JSON.parse(document.querySelector('#az-data').textContent);let n=0;for(const e of D.entries){for(const f of e.forms){const a=f.word.match(/.{2}/g);const swap=[a[1],a[0],a[2]].join('');const unswap=[a[0],a[1],a[2]].join('');if(T.inspect(swap).entry.root!==e.root||T.inspect(unswap).entry.root!==e.root)throw Error('Swap escaped root');const rot=[a[1],a[2],a[0]].join('');if(T.inspect(rot).entry.root!==e.root)throw Error('Rotation escaped root');const p=T.serialize(f.word);if(T.decodePayload(p).form.word!==f.word)throw Error('Payload failed');n++;}}return n;}''')
  self.assertEqual(600,result)
 def test_practice_first_try_then_wrong_then_correct(self):
  self.nav('practice');t=self.page.evaluate('window.AZURAVEL_TEST.trialDescriptor()')
  wrong=next(f['word'] for f in t['root']['forms'] if f['word']!=t['form']['word'])
  self.page.locator(f'[data-choice="{wrong}"]').click()
  self.assertEqual('true',self.page.locator('#practice-feedback').get_attribute('data-error'))
  self.assertIn('0 first-try',self.page.locator('#practice-score').inner_text())
  self.page.locator(f'[data-choice="{t["form"]["word"]}"]').click()
  self.assertTrue(self.page.locator('#practice-next').is_enabled())
  self.page.locator('#practice-next').click()
  self.assertIn('TRIAL 2',self.page.locator('#practice-count').inner_text())
  self.assertEqual('0 first-try matches',self.page.locator('#practice-score').inner_text())
 def test_practice_all_12_rounds_with_exact_correct_choices(self):
  self.nav('practice')
  for i in range(12):
   answer=self.page.evaluate('window.AZURAVEL_TEST.trialDescriptor().form.word')
   self.page.locator(f'[data-choice="{answer}"]').click()
   self.assertIn(str(i+1)+' first-try',self.page.locator('#practice-score').inner_text())
   if i<11:self.page.locator('#practice-next').click()
  self.page.locator('#practice-next').click()
  self.assertIn('COMPLETE',self.page.locator('#practice-count').inner_text())
  self.assertIn('12 / 12',self.page.locator('#practice-score').inner_text())
  self.page.locator('#practice-reset').click();self.assertIn('TRIAL 1',self.page.locator('#practice-count').inner_text())
 def test_invalid_words_still_rejected(self):
  self.page.locator('#word-input').fill('abcdef');self.page.locator('#inspect-btn').click()
  self.assertEqual('true',self.page.locator('#word-status').get_attribute('data-error'))
 def test_original_compiler_still_rejects_illegal_reciprocal(self):
  self.nav('syntax');self.page.locator('#b-lo').check()
  self.assertEqual('true',self.page.locator('#build-status').get_attribute('data-error'))
 def test_contained_english_still_rejects_unregistered(self):
  self.nav('translate');self.page.locator('#english-input').fill('I will teleport');self.page.locator('#english-convert').click()
  self.assertEqual('true',self.page.locator('#english-result').get_attribute('data-error'))
 def test_20_sentences_still_parse(self):
  self.assertEqual(20,self.page.evaluate('''()=>{const a=JSON.parse(document.querySelector('#az-data').textContent).sentences;for(const s of a)window.AZURAVEL_TEST.parseAZ(s.az);return a.length;}'''))
 def test_hash_updates_with_surface_word(self):
  self.page.locator('#loom-swap').click()
  self.assertTrue(self.page.evaluate('window.location.hash').endswith('/I01/12'))
 def test_route_deep_link_can_restore_exact_word(self):
  self.page.evaluate("window.location.hash='#lab/I01/12'")
  self.page.wait_for_timeout(80)
  self.assertEqual('romike',self.page.locator('#selected-word .word').inner_text())
 def test_reduced_motion_disables_loom_animation(self):
  reduced=self.browser.new_page(reduced_motion='reduce')
  try:
   reduced.set_content(HTML,wait_until='load')
   actual=reduced.evaluate('getComputedStyle(document.querySelector("#loom-lines svg path")).animationName')
   self.assertEqual('none',actual)
  finally:reduced.close()
 def test_no_external_assets_or_requests(self):
  requests=[];pg=self.browser.new_page()
  pg.on('request',lambda req:requests.append(req.url))
  try:
   pg.set_content(HTML,wait_until='load');self.assertEqual([],requests)
   self.assertFalse('https://' in HTML[:2500])
  finally:pg.close()
 def test_artifact_single_file_and_rebuild_template(self):
  self.assertTrue((ROOT/'development/atlas_template_base.html').exists())
  self.assertTrue((ROOT/'development/uplift.js').exists())
  self.assertTrue((ROOT/'development/uplift.css').exists())
  self.assertEqual(6,len(BeautifulSoup(HTML,'html.parser').select('section.view')))
 def test_simulated_storage_roundtrip_restore_word_and_practice(self):
  self.page.evaluate("""() => {const db={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>db[k]||null,setItem:(k,v)=>db[k]=v,removeItem:k=>delete db[k]}});}""")
  self.page.locator('#loom-swap').click()
  self.nav('practice')
  target=self.page.evaluate('window.AZURAVEL_TEST.trialDescriptor()')
  wrong=next(f['word'] for f in target['root']['forms'] if f['word']!=target['form']['word'])
  self.page.locator(f'[data-choice="{wrong}"]').click()
  stored=json.loads(self.page.evaluate("localStorage.getItem('azuravel.lab.1.1')"))
  self.assertEqual('romike',stored['word']);self.assertEqual('practice',stored['view'])
  self.assertEqual([wrong],stored['practice']['wrongWords'])
  self.page.set_content(HTML,wait_until='load')
  self.assertEqual('romike',self.page.locator('#selected-word .word').inner_text())
  self.assertTrue(self.page.locator('#view-practice').is_visible())
  self.assertTrue(self.page.locator(f'[data-choice="{wrong}"]').is_disabled())
  self.assertIn('Saved on this device',self.page.locator('#workspace-status').inner_text())
 def test_self_contained_rebuild_in_clean_directory(self):
  import tempfile,shutil,subprocess,sys
  with tempfile.TemporaryDirectory() as td:
   location=Path(td)/'project'
   shutil.copytree(ROOT,location,ignore=shutil.ignore_patterns('__pycache__','*.png','*.log'))
   expected=hashlib.sha256((location/'AZURAVEL_ATLAS.html').read_bytes()).hexdigest()
   p=subprocess.run([sys.executable,'development/build_uplift.py'],cwd=location,capture_output=True,text=True)
   self.assertEqual(0,p.returncode,p.stderr)
   self.assertEqual(expected,hashlib.sha256((location/'AZURAVEL_ATLAS.html').read_bytes()).hexdigest())
 def test_browser_session_storage_graceful_fallback(self):
  self.assertTrue(self.page.locator('#selected-word .word').is_visible())
  self.assertIn('Session only',self.page.locator('#workspace-status').inner_text())

if __name__=='__main__':unittest.main()
