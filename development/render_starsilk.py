from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
root=Path(__file__).resolve().parent.parent
page_html=(root/'index.html').read_text()
poster=base64.b64encode((root/'assets/ribbon-poster.jpg').read_bytes()).decode()
page_html=page_html.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+poster).replace('src="./assets/azuravel-ribbons.mp4"','src=""')
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(1440,900),(390,844),(320,700)]:
  page=b.new_page(viewport={'width':w,'height':h},reduced_motion='reduce')
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(page_html,wait_until='load')
  page.locator('#enter-testimony').click()
  for i in range(4):
   page.evaluate('(i)=>AZURAVEL_OBSERVATORY_TEST.openWitness(i)',i)
   page.screenshot(path=str(root/f'evidence/witness_{i}_claim_{w}.png'))
   page.evaluate("AZURAVEL_OBSERVATORY_TEST.openWitnessLens('cost')")
   page.screenshot(path=str(root/f'evidence/witness_{i}_cost_{w}.png'))
  print(w,{'errors':errors,'phase':page.locator('#observatory').get_attribute('data-phase'),'overflow':page.evaluate('document.documentElement.scrollWidth-innerWidth')})
  page.close()
 b.close()
