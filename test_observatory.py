"""Observable browser and source regression checks for the AZURAVEL Unwitnessed Index."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import unittest, json, hashlib, base64, subprocess, tempfile, shutil, sys
from azuravel_ref import transform, inspect_word, payload, decode_payload, parse_sentence

ROOT=Path(__file__).resolve().parent
HTML=(ROOT/'index.html').read_text(encoding='utf-8')
DATA=json.loads((ROOT/'AZURAVEL_DATA.json').read_text(encoding='utf-8'))
POSTER=base64.b64encode((ROOT/'assets/ribbon-poster.jpg').read_bytes()).decode('ascii')
TEST_HTML=HTML.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+POSTER).replace('src="./assets/azuravel-ribbons.mp4"','src=""')

class ObservatoryTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.playwright=sync_playwright().start()
  cls.browser=cls.playwright.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 @classmethod
 def tearDownClass(cls):cls.browser.close();cls.playwright.stop()
 def setUp(self):
  self.page=self.browser.new_page(viewport={'width':1440,'height':900},reduced_motion='reduce')
  self.errors=[];self.page.on('pageerror',lambda e:self.errors.append(str(e)))
  self.page.set_content(TEST_HTML,wait_until='load')
 def tearDown(self):
  self.assertEqual([],self.errors,'No unhandled browser JS errors')
  self.page.close()
 def enter(self):self.page.locator('#enter-observatory').click()
 def go_root(self):
  self.enter()
  self.page.locator('.glyph-node[data-kind=domain]').first.click()
  self.page.locator('.glyph-node[data-kind=root]').first.click()
 def state(self):return self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.snapshot()')
 def test_exact_normative_data_embedded(self):
  actual=self.page.evaluate("JSON.parse(document.querySelector('#az-data').textContent)")
  self.assertEqual(DATA,actual)
 def test_immutable_language_contract(self):
  self.assertEqual(100,len(DATA['entries']))
  self.assertEqual(600,sum(len(e['forms']) for e in DATA['entries']))
  for e in DATA['entries']:
   for f in e['forms']:
    self.assertEqual(transform(e['root'],int(f['state'][0]),int(f['state'][1])),f['word'])
    self.assertEqual(e['id'],inspect_word(f['word'])['id'])
    self.assertEqual(f['word'],decode_payload(payload(f['word']))['surface'])
 def test_source_preservation(self):
  manifest=json.loads((ROOT/'PROTECTED_HASHES.json').read_text())
  for name,sha in manifest.items():
   self.assertEqual(sha,hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),name)
 def test_threshold_significance_and_entry(self):
  self.assertTrue(self.page.locator('#threshold').is_visible());self.assertTrue(self.page.locator('#field').is_hidden())
  self.assertIn('wrong thing',self.page.locator('#threshold-title').inner_text())
  self.enter();self.assertTrue(self.page.locator('#field').is_visible());self.assertTrue(self.page.locator('#threshold').is_hidden())
  self.assertEqual(10,self.page.locator('.glyph-node[data-kind=domain]').count())
 def test_all_ten_sectors_expose_ten_real_roots(self):
  self.enter()
  for d in dict.fromkeys(e['domain'] for e in DATA['entries']):
   self.page.evaluate('(d)=>AZURAVEL_OBSERVATORY_TEST.openDomain(d)',d)
   self.assertEqual(10,self.page.locator('.glyph-node[data-kind=root]').count())
   self.assertIn(d,self.page.locator('#reader-title').inner_text())
 def test_all_six_forms_accessible_through_real_controls(self):
  self.go_root();self.assertEqual('I01',self.state()['id'])
  self.assertEqual(6,self.page.locator('.glyph-node[data-kind=form]').count())
  for f in DATA['entries'][0]['forms']:
   self.page.locator('.glyph-node[data-kind=form][aria-label^="'+f['role']+'"]') .click()
   self.assertEqual(f['state'],self.state()['state'])
   self.assertEqual(f['word'],self.page.locator('#large-word').inner_text())
   self.assertIn(f['meaning'],self.page.locator('#reader-lead').inner_text())
   self.assertEqual(f['word'],''.join(self.page.locator('.large-syllables span').all_inner_texts()))
 def test_counteraction_not_negation(self):
  self.go_root();self.page.locator('.glyph-node[data-kind=form][aria-label^="CTR"]').click()
  self.assertIn('not confuse',self.page.locator('#reader-sub').inner_text())
  self.page.locator('.reader-actions .primary-action').first.click()
  self.assertEqual('differential',self.state()['phase'])
  self.assertEqual('sa miroke',self.page.locator('#absence-form').inner_text())
  self.assertEqual('romike',self.page.locator('#counter-form').inner_text())
  self.assertIn('not nothing',self.page.locator('#reader-title').inner_text())
 def test_contrast_is_per_root_not_fake_literal(self):
  self.enter();self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRoot('I06','00')")
  self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.contrast()')
  e=next(e for e in DATA['entries'] if e['id']=='I06')
  self.assertEqual('sa '+e['forms'][1]['word'],self.page.locator('#absence-form').inner_text())
  self.assertEqual(e['forms'][5]['word'],self.page.locator('#counter-form').inner_text())
 def test_case_file_unlock_is_ordered_not_fake(self):
  self.enter();self.assertEqual(1,self.state()['availableRecords'])
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRoot('I01')")
  self.assertEqual(2,self.state()['availableRecords'])
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRoot('I02')")
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRoot('I03')")
  self.assertEqual(2,self.state()['availableRecords'],'One cannot skip the counter-event gate')
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRole('12')")
  self.assertEqual(4,self.state()['availableRecords'])
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRoot('I04')")
  self.assertEqual(4,self.state()['availableRecords'])
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRole('01')")
  self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openRole('02')")
  self.assertEqual(5,self.state()['availableRecords'])
  self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.openRecord(4)')
  self.assertIn('second person',self.page.locator('#reader-title').inner_text().lower())
 def test_records_explicitly_not_canonical(self):
  self.enter();self.page.locator('#rail-records').click()
  self.assertIn('SPECULATIVE / NOT CANON',self.page.locator('#reader-kind').inner_text())
  self.assertIn('marote',self.page.locator('#reader-source').inner_text())
  self.assertIn('cannot',self.page.locator('#reader-sub').inner_text())
 def test_reader_transcript_single_scroll_surface(self):
  self.enter();self.page.locator('#rail-records').click()
  self.assertEqual('auto',self.page.evaluate('getComputedStyle(document.querySelector("#reader-transcript")).overflowY'))
 def test_deterministic_file_entry(self):
  with tempfile.TemporaryDirectory() as td:
   temp=Path(td)
   (temp/'development').mkdir()
   (temp/'sources').mkdir()
   shutil.copyfile(ROOT/'sources/starsilk_testimony.json',temp/'sources/starsilk_testimony.json')
   for x in ['observatory_template.html','observatory.js','observatory.css','build_observatory.py']:
    shutil.copyfile(ROOT/'development'/x,temp/'development'/x)
   shutil.copyfile(ROOT/'AZURAVEL_DATA.json',temp/'AZURAVEL_DATA.json')
   r=subprocess.run([sys.executable,'development/build_observatory.py'],cwd=temp,text=True,capture_output=True)
   self.assertEqual(0,r.returncode,r.stderr)
   self.assertEqual(hashlib.sha256((temp/'index.html').read_bytes()).hexdigest(),hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest())
 def test_no_runtime_dependency_or_tracking(self):
  self.assertNotIn('<script src=',HTML.lower())
  self.assertNotIn('@import',HTML)
  self.assertNotIn('fetch(',HTML)
  self.assertNotIn('sendBeacon(',HTML)
  self.assertNotIn('analytics',HTML.lower())
  self.assertNotIn('localstorage.clear(',HTML.lower())
 def test_no_default_audio(self):
  self.assertEqual('false',self.page.locator('#sound-toggle').get_attribute('aria-pressed'))
  self.assertEqual('SOUND OFF',self.page.locator('#sound-label').inner_text())
 def test_reduced_motion_has_static_fallback(self):
  self.assertEqual('none',self.page.evaluate("getComputedStyle(document.querySelector('#ribbon-film')).display"))
  self.enter();self.assertEqual(10,self.page.locator('.glyph-node').count())
 def test_mobile_desktop_navigation_and_chrome_coverage(self):
  for w,h in [(320,700),(360,780),(390,844),(768,900),(1024,768),(1440,900)]:
   self.page.set_viewport_size({'width':w,'height':h})
   self.page.goto('about:blank')
   self.page.set_content(TEST_HTML,wait_until='load')
   self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),w+1)
   self.enter();self.page.locator('.glyph-node').first.click();self.page.locator('.glyph-node').first.click()
   self.assertEqual(6,self.page.locator('.glyph-node[data-kind=form]').count())
   self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),w+1)
   metrics=self.page.evaluate('''()=>{const els=[document.querySelector('.masthead'),document.querySelector('.reader'),document.querySelector('.strata-rail'),...document.querySelectorAll('.glyph-node')];let area=0;for(const el of els){if(!el||!el.getClientRects().length)continue;const r=el.getBoundingClientRect();area+=Math.max(0,Math.min(innerWidth,r.right)-Math.max(0,r.left))*Math.max(0,Math.min(innerHeight,r.bottom)-Math.max(0,r.top));}return {fraction:area/(innerWidth*innerHeight),panel:document.querySelector('.reader').getBoundingClientRect().height/innerHeight}}''')
   self.assertLess(metrics['fraction'],.4,(w,metrics))
   self.assertLessEqual(metrics['panel'],.38,(w,metrics))
   self.page.locator('#rail-index').click()
 def test_escape_navigation(self):
  self.go_root();self.page.locator('body').focus();self.page.keyboard.press('Escape')
  self.assertEqual('roots',self.state()['phase']);self.page.keyboard.press('Escape');self.assertEqual('sectors',self.state()['phase'])
 def test_controls_have_accessible_names(self):
  self.enter()
  for q in ['#motion-toggle','#sound-toggle','.laboratory-link','#rail-index','#rail-records','#rail-contrast']:
   self.assertTrue(self.page.locator(q).get_attribute('aria-label'),q)
 def test_lab_handoff_matches_exact_route(self):
  self.go_root();self.page.locator('.glyph-node[aria-label^="CTR"]').click()
  href=self.page.locator('.reader-actions a[href*="AZURAVEL_ATLAS.html"]').get_attribute('href')
  self.assertEqual('./AZURAVEL_ATLAS.html#lab/I01/12',href)
 def test_all_twenty_authoritative_examples_parse(self):
  for s in DATA['sentences']: self.assertTrue(parse_sentence(s['az']),s['az'])

if __name__=='__main__':unittest.main()
