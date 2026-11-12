from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text()
poster=base64.b64encode((root/'assets/ribbon-poster.jpg').read_bytes()).decode()
html=html.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+poster).replace('src="./assets/azuravel-ribbons.mp4"','src=""')
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in ((1440,900),(390,844),(320,700),(320,568)):
  p=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce',device_scale_factor=1)
  p.set_content(html,wait_until='load')
  for stage in range(3):
   p.evaluate('(n)=>{location.hash="ledger="+n;}',stage)
   p.wait_for_timeout(100)
   p.screenshot(path=str(root/'evidence/omni'/f'ledger_{stage}_{width}x{height}.png'))
  p.close()
 browser.close()
print('Captured 12 browser states')
