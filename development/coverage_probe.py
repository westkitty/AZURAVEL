from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text()
poster=base64.b64encode((root/'assets/ribbon-poster.jpg').read_bytes()).decode()
html=html.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+poster).replace('src="./assets/azuravel-ribbons.mp4"','src=""')
JS='''()=>{const els=[document.querySelector('.masthead'),document.querySelector('.reader'),document.querySelector('.strata-rail'),...document.querySelectorAll('.glyph-node')];let area=0;for(const el of els){if(!el||!el.getClientRects().length)continue;const r=el.getBoundingClientRect();area+=Math.max(0,Math.min(innerWidth,r.right)-Math.max(0,r.left))*Math.max(0,Math.min(innerHeight,r.bottom)-Math.max(0,r.top));}return {fraction:area/(innerWidth*innerHeight),panel:document.querySelector('.reader').getBoundingClientRect().height/innerHeight,overflow:document.documentElement.scrollWidth-innerWidth}}'''
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(320,700),(360,780),(390,844),(768,900),(1024,768),(1440,900)]:
  page=b.new_page(viewport={'width':w,'height':h},reduced_motion='reduce');page.set_content(html)
  paths=[('threshold',lambda:None),('sectors',lambda:page.locator('#enter-observatory').click()),('roots',lambda:page.locator('.glyph-node[data-kind=domain]').first.click()),('forms',lambda:page.locator('.glyph-node[data-kind=root]').first.click()),('counter',lambda:page.locator('.glyph-node[data-kind=form]').last.click()),('difference',lambda:page.evaluate('AZURAVEL_OBSERVATORY_TEST.contrast()')),('records',lambda:page.locator('#rail-records').click())]
  for name,enter in paths:
   enter();m=page.evaluate(JS); print(w,name,m)
   if name!='threshold' and (m['fraction']>=.4 or m['panel']>.38 or m['overflow']>1):raise SystemExit('UI CEILING FAIL: '+str((w,name,m)))
  page.close()
 b.close()
