"""Regression proof for source-bound four-record consequence ledger."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import base64,json,unittest
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'AZURAVEL_DATA.json').read_text())
STAR=json.loads((ROOT/'sources/starsilk_testimony.json').read_text())
HTML=(ROOT/'index.html').read_text()
POSTER=base64.b64encode((ROOT/'assets/ribbon-poster.jpg').read_bytes()).decode()
BROWSER_HTML=HTML.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+POSTER).replace('src="./assets/azuravel-ribbons.mp4"','src=""')
class LedgerJourney(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.pw=sync_playwright().start()
  cls.browser=cls.pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 @classmethod
 def tearDownClass(cls):
  cls.browser.close();cls.pw.stop()
 def setUp(self):
  self.page=self.browser.new_page(viewport={'width':1440,'height':900},reduced_motion='reduce')
  self.errors=[]
  self.page.on('pageerror',lambda e:self.errors.append(str(e)))
  self.page.set_content(BROWSER_HTML,wait_until='load')
 def tearDown(self):
  self.assertEqual([],self.errors)
  self.page.close()
 def snapshot(self):return self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.snapshot()')
 def collect(self):
  self.page.locator('#enter-testimony').click()
  for i in range(4):
   self.page.evaluate('(i)=>AZURAVEL_OBSERVATORY_TEST.openWitness(i)',i)
   self.page.evaluate("AZURAVEL_OBSERVATORY_TEST.openWitnessLens('cost')")
  self.assertEqual(4,self.snapshot()['witnessViewed'])
 def test_ledger_is_not_claimed_prematurely(self):
  self.page.locator('#enter-testimony').click()
  self.assertEqual(0,self.page.get_by_role('button',name='Assemble the unclosed ledger').count())
  self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.openLedger(0)')
  self.assertEqual('witness',self.snapshot()['phase'])
  self.assertIn('incomplete',self.page.locator('#event-announcer').inner_text())
 def test_four_readings_unlock_and_reclassification(self):
  self.collect()
  self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  self.assertEqual('ledger',self.snapshot()['phase'])
  self.assertEqual(0,self.snapshot()['ledgerStage'])
  self.assertIn('It worked.',self.page.locator('#reader-title').inner_text())
  self.assertIn('separate source records',self.page.locator('#reader-sub').inner_text())
  self.assertEqual(3,self.page.locator('.glyph-node[data-kind=ledger]').count())
 def test_all_three_readings_and_intimate_end(self):
  self.collect()
  self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  self.page.get_by_role('button',name='Expose the cost').click()
  self.assertEqual(1,self.snapshot()['ledgerStage'])
  self.assertIn('Nacreous VI survived',self.page.locator('#reader-sub').inner_text())
  self.page.get_by_role('button',name='Go to the cup').click()
  self.assertEqual(2,self.snapshot()['ledgerStage'])
  self.assertIn('I became necessary. That is not the same thing.',self.page.locator('#reader-sub').inner_text())
  self.assertIn('not another Blood Ring',self.page.locator('#reader-sub').inner_text())
  self.page.get_by_role('button',name='Return to the four').click()
  self.assertEqual(0,self.snapshot()['ledgerStage'])
 def test_keyboard_access_to_all_three_stages(self):
  self.collect();self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  for i in [1,2,0]:
   b=self.page.locator('.glyph-node[data-kind=ledger]').nth(i)
   b.focus();self.page.keyboard.press('Enter')
   self.assertEqual(i,self.snapshot()['ledgerStage'])
  self.page.keyboard.press('Escape')
  self.assertEqual('witness',self.snapshot()['phase'])
 def test_deep_link_to_final_reading(self):
  self.page.evaluate("location.hash='ledger=2'")
  self.page.wait_for_timeout(60)
  self.assertEqual('ledger',self.snapshot()['phase'])
  self.assertEqual(2,self.snapshot()['ledgerStage'])
  self.assertEqual('2',self.page.locator('#observatory').get_attribute('data-ledger-stage'))
 def test_malformed_saved_progress_does_not_break_entry(self):
  payload='{"visited":{"unexpected":true},"roles":24,"witnessSeen":"not-a-list","counter":true}'
  prelude="<script>Object.defineProperty(window, 'localStorage', { configurable: true, value:{getItem:()=>JSON.stringify({visited:{unexpected:true},roles:24,witnessSeen:'not-a-list',counter:true}),setItem:()=>{}}});</script>"
  injected=BROWSER_HTML.replace('<script id="az-data"',prelude+'<script id="az-data"',1)
  page=self.browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce')
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  try:
   page.set_content(injected,wait_until='load')
   page.locator('#enter-testimony').click()
   snap=page.evaluate('AZURAVEL_OBSERVATORY_TEST.snapshot()')
   self.assertEqual('witness',snap['phase'])
   self.assertEqual(0,snap['witnessViewed'])
   self.assertEqual([],errors)
  finally:page.close()
 def test_short_phone_keeps_text_and_controls_operable(self):
  self.page.set_viewport_size({'width':320,'height':568})
  self.collect()
  self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  self.page.get_by_role('button',name='Expose the cost').click()
  self.page.get_by_role('button',name='Go to the cup').click()
  self.assertEqual(2,self.snapshot()['ledgerStage'])
  visible=self.page.evaluate("document.querySelector('#reader-transcript').getBoundingClientRect().height")
  self.assertGreaterEqual(visible,26)
  self.assertEqual('auto',self.page.evaluate("getComputedStyle(document.querySelector('#reader-transcript')).overflowY"))
  self.page.locator('#reader-transcript').evaluate('(e)=>e.scrollTop=e.scrollHeight')
  self.assertGreater(self.page.evaluate("document.querySelector('#reader-transcript').scrollTop"),0)
  self.page.get_by_role('button',name='Return to the four').click()
  self.assertEqual(0,self.snapshot()['ledgerStage'])
 def test_origins_stay_separate(self):
  self.assertEqual(100,len(DATA['entries']))
  self.assertEqual(600,sum(len(e['forms']) for e in DATA['entries']))
  self.assertEqual(4,len(STAR['cases']))
  self.assertIn('not a Starsilk translation',STAR['cases'][0]['root_reason'])
  self.assertNotIn('fetch(',HTML)
  self.assertNotIn('<script src=',HTML)
 def test_three_stages_under_40_percent(self):
  self.collect();self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  for width,height in [(320,568),(320,700),(390,844),(768,900),(1440,900)]:
   self.page.set_viewport_size({'width':width,'height':height})
   for stage in range(3):
    self.page.evaluate('(i)=>AZURAVEL_OBSERVATORY_TEST.openLedger(i)',stage)
    measured=self.page.evaluate('''()=>{let a=0;for(const el of [document.querySelector('.masthead'),document.querySelector('.reader'),document.querySelector('.strata-rail'),...document.querySelectorAll('.glyph-node')]){if(!el.getClientRects().length)continue;const r=el.getBoundingClientRect();a+=Math.max(0,Math.min(innerWidth,r.right)-Math.max(0,r.left))*Math.max(0,Math.min(innerHeight,r.bottom)-Math.max(0,r.top));}return {coverage:a/(innerWidth*innerHeight),overflow:document.documentElement.scrollWidth-innerWidth};}''')
    self.assertLess(measured['coverage'],.4,(width,stage,measured))
    self.assertLessEqual(measured['overflow'],1,(width,stage,measured))
 def test_source_language_boundary_is_visible_at_climax(self):
  self.collect();self.page.get_by_role('button',name='Assemble the unclosed ledger').click()
  self.page.evaluate('AZURAVEL_OBSERVATORY_TEST.openLedger(2)')
  self.assertIn('NOT AZ1',self.page.locator('#reader-source').inner_text())
  self.assertIn('STARSILK',self.page.locator('#reader-kind').inner_text())
  self.assertEqual(4,self.snapshot()['witnessViewed'])
if __name__=='__main__':unittest.main()
