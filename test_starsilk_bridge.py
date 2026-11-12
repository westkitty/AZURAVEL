"""Project-source witness lens: semantic boundary and real browser paths."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import hashlib,json,unittest,base64,os
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'AZURAVEL_DATA.json').read_text())
STAR=json.loads((ROOT/'sources/starsilk_testimony.json').read_text())
HTML=(ROOT/'index.html').read_text(encoding='utf-8')
POSTER=base64.b64encode((ROOT/'assets/ribbon-poster.jpg').read_bytes()).decode('ascii')
TEST_HTML=HTML.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+POSTER).replace('src="./assets/azuravel-ribbons.mp4"','src=""')

class CaseArchive(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.play=sync_playwright().start()
  cls.browser=cls.play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 @classmethod
 def tearDownClass(cls):cls.browser.close();cls.play.stop()
 def setUp(self):
  self.page=self.browser.new_page(viewport={'width':1440,'height':900},reduced_motion='reduce')
  self.errors=[]
  self.page.on('pageerror',lambda e:self.errors.append(str(e)))
  self.page.set_content(TEST_HTML,wait_until='load')
 def tearDown(self):
  self.assertFalse(self.errors,self.errors)
  self.page.close()
 def state(self):return self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.snapshot()')
 def test_authorial_source_anchored(self):
  src=Path(os.environ.get("AZURAVEL_TESTIMONY_SOURCE","/nonexistent/azuravel-testimony-source.txt"))
  self.assertEqual(4,len(STAR['cases']))
  if src.exists():
   self.assertEqual(STAR['source_sha256'],hashlib.sha256(src.read_bytes()).hexdigest())
   lines=src.read_text()
  else: lines=None
  for case in STAR['cases']:
   if lines is not None:self.assertIn(case['primary_evidence'],lines)
   self.assertIn(case['root_id'],[e['id'] for e in DATA['entries']])
  self.assertIn('not a Starsilk translation',STAR['cases'][0]['root_reason'])
 def test_source_and_language_distinct(self):
  self.assertIn('NOT AZ1 LANGUAGE CANON',STAR['status'])
  self.assertIn('independent constructed language',STAR['source_boundaries'][0])
  self.assertEqual(DATA,self.page.evaluate("JSON.parse(document.querySelector('#az-data').textContent)"))
  self.assertEqual(STAR,self.page.evaluate("JSON.parse(document.querySelector('#starsilk-data').textContent)"))
 def test_threshold_entry_and_reading(self):
  self.page.locator('#enter-testimony').click()
  self.assertEqual('witness',self.state()['phase'])
  self.assertIn('memorial image',self.page.locator('#reader-title').inner_text())
  self.assertEqual('STARSILK / CLAIM',self.page.locator('#reader-kind').inner_text())
  self.assertIn('SOURCE-BOUND',self.page.locator('#reader-source').inner_text())
  self.assertIn('AUTHORIAL STARSILK TESTIMONY',self.page.locator('#scene-designation').inner_text())
  self.assertEqual(4,self.page.locator('.glyph-node[data-kind=witness]').count())
  self.page.get_by_role('button',name='Examine the cost').click()
  self.assertIn('made of the civilization',self.page.locator('#reader-lead').inner_text())
  self.assertIn('They were not symbols.',self.page.locator('#reader-sub').inner_text())
  self.assertEqual('cost',self.state()['witnessLens'])
 def test_four_cases_and_bilateral_lens(self):
  self.page.locator('#enter-observatory').click()
  for index,record in enumerate(STAR['cases']):
   self.page.evaluate('(i)=>AZURAVEL_OBSERVATORY_TEST.openWitness(i)',index)
   self.assertIn(record['claim']['lead'],self.page.locator('#reader-lead').inner_text())
   self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openWitnessLens('cost')")
   self.assertIn(record['cost']['lead'],self.page.locator('#reader-lead').inner_text())
   self.assertIn(record['primary_evidence'],self.page.locator('#reader-sub').inner_text())
   self.assertIn('SCHEMATIC',self.page.locator('#horizon-bottom').inner_text())
  self.assertEqual(4,self.state()['witnessViewed'])
 def test_lexical_analogy_and_return(self):
  self.page.locator('#enter-testimony').click()
  self.page.get_by_role('button',name='Trace memory in AZ1').click()
  self.assertEqual('forms',self.state()['phase'])
  self.assertEqual('I06',self.state()['id'])
  self.page.get_by_role('button',name='Return to testimony').click()
  self.assertEqual('witness',self.state()['phase'])
 def test_witness_deep_link(self):
  self.page.evaluate("location.hash='witness=nacreous-six&lens=cost'")
  self.page.wait_for_timeout(80)
  self.assertEqual('witness',self.state()['phase'])
  self.assertEqual(2,self.state()['witnessIndex'])
  self.assertIn('Level 3 remnant',self.page.locator('#reader-lead').inner_text())
 def test_speculative_case_files_unaltered(self):
  self.page.locator('#enter-observatory').click()
  self.page.locator('#rail-records').click()
  self.assertIn('SPECULATIVE / NOT CANON',self.page.locator('#reader-kind').inner_text())
  self.page.locator('#rail-witness').click()
  self.assertIn('STARSILK / CLAIM',self.page.locator('#reader-kind').inner_text())
 def test_source_metadata_does_not_become_fake_signal(self):
  self.assertNotIn('fetch(',HTML)
  self.assertNotIn('<script src=',HTML.lower())
  self.assertNotIn('sendBeacon',HTML)
  self.assertNotIn('STARSILK CASES ARE AZ1 HISTORY',HTML)
 def test_mobile_reader_and_coverage(self):
  for width,height in [(320,700),(390,844),(768,900),(1440,900)]:
   self.page.set_viewport_size({'width':width,'height':height})
   self.page.locator('#enter-testimony').click() if self.state()['phase']=='threshold' else None
   for i in range(4):
    self.page.evaluate('(i)=>AZURAVEL_OBSERVATORY_TEST.openWitness(i)',i)
    self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openWitnessLens('cost')")
    area=self.page.evaluate('''()=>{let total=0;for(const el of [document.querySelector('.masthead'),document.querySelector('.reader'),document.querySelector('.strata-rail'),...document.querySelectorAll('.glyph-node')]){if(!el||!el.getClientRects().length)continue;const r=el.getBoundingClientRect();total+=Math.max(0,Math.min(innerWidth,r.right)-Math.max(0,r.left))*Math.max(0,Math.min(innerHeight,r.bottom)-Math.max(0,r.top));}return total/(innerWidth*innerHeight);}''')
    self.assertLess(area,.4,(width,i,area))
    self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width+1,(width,i))
    self.assertEqual('auto',self.page.evaluate('getComputedStyle(document.querySelector("#reader-transcript")).overflowY'))

if __name__=='__main__':unittest.main()
