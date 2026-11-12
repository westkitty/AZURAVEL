from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
ROOT=Path(__file__).resolve().parent.parent
html=(ROOT/'index.html').read_text()
poster=base64.b64encode((ROOT/'assets/ribbon-poster.jpg').read_bytes()).decode('ascii')
html=html.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+poster)
# Source page routes are not permitted from the browser sandbox. Rendering uses the same document bytes and inline poster.
html=html.replace('src="./assets/azuravel-ribbons.mp4"','src=""')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for w,h in [(1440,900),(390,844),(320,700)]:
  page=b.new_page(viewport={'width':w,'height':h},reduced_motion='reduce')
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(html,wait_until='load')
  page.screenshot(path=str(ROOT/f'evidence/threshold_{w}.png'))
  page.locator('#enter-observatory').click()
  page.screenshot(path=str(ROOT/f'evidence/sectors_{w}.png'))
  page.locator('.glyph-node').first.click()
  page.screenshot(path=str(ROOT/f'evidence/roots_{w}.png'))
  page.locator('.glyph-node').first.click()
  page.screenshot(path=str(ROOT/f'evidence/forms_{w}.png'))
  page.locator('.glyph-node[data-kind=form]').last.click()
  page.screenshot(path=str(ROOT/f'evidence/counter_{w}.png'))
  page.locator('.primary-action').first.click()
  page.screenshot(path=str(ROOT/f'evidence/difference_{w}.png'))
  print(w,{'errors':errors,'phase':page.locator('#observatory').get_attribute('data-phase'),'overflow':page.evaluate('document.documentElement.scrollWidth-innerWidth'),'nodes':page.locator('.glyph-node').count(),'head':page.locator('#reader-title').inner_text()})
  page.close()
 b.close()
