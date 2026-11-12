"""Build a deterministic AZURAVEL local review package; does not publish it."""
from pathlib import Path
import base64,hashlib,json,zipfile
R=Path(__file__).resolve().parent.parent
OUT=R.parent
html=(R/'index.html').read_text()
poster=base64.b64encode((R/'assets/ribbon-poster.jpg').read_bytes()).decode('ascii')
film=base64.b64encode((R/'assets/azuravel-ribbons.mp4').read_bytes()).decode('ascii')
assert './assets/ribbon-poster.jpg' in html
assert 'src="./assets/azuravel-ribbons.mp4"' in html
html=html.replace('./assets/ribbon-poster.jpg','data:image/jpeg;base64,'+poster).replace('src="./assets/azuravel-ribbons.mp4"','src="data:video/mp4;base64,'+film+'"')
assert 'src="./assets/' not in html
(OUT/'AZURAVEL_Unclosed_Ledger_Offline.html').write_text(html)
preview=R/'evidence/omni/ledger_2_1440x900.png'
(OUT/'AZURAVEL_Unclosed_Ledger_Preview.png').write_bytes(preview.read_bytes())
manifest=json.loads((R/'SITE_MANIFEST.json').read_text())
manifest['release']='unclosed-ledger-local-review-1'
manifest['evidence_scope']='150 isolated-suite tests PASS, 102 prior + 15 new geometric observations; unclosed ledger local artifact, no new GitHub commit or Pages deploy'
paths={x['path'] for x in manifest['files']}
for extra in ('AZURAVEL_bible.md','OMNI_QQQ_AWE_REPORT.md','test_ledger.py','development/preview_ledger.py','development/build_release_ledger.py'):
 paths.add(extra)
manifest['files']=[{'path':p,'size':(R/p).stat().st_size,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()} for p in sorted(paths)]
(R/'SITE_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
selected=[p for p in sorted(paths) if not p.startswith('evidence/')]+['SITE_MANIFEST.json']
selected=list(dict.fromkeys(selected))
selected+=['evidence/omni/'+p.name for p in sorted((R/'evidence/omni').glob('ledger_*.png'))]
selected+=['evidence/omni/'+p for p in ['baseline_corrupt_storage.txt','uplift_corrupt_storage.txt','ledger_regression.log','observatory_regression.log','starsilk_regression.log','original_coverage.log','sha_1.txt','sha_2.txt','build_output.log']]
selected=list(dict.fromkeys(selected))
zip_path=OUT/'AZURAVEL_Unclosed_Ledger_Source_2026-11-12.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for p in selected:
  if not (R/p).is_file():raise FileNotFoundError(p)
  z.write(R/p,p)
 with z.open('OFFLINE_REVIEW.txt','w') as f:
  f.write(b'Offline standalone HTML is distributed separately as AZURAVEL_Unclosed_Ledger_Offline.html. No GitHub commit or Pages deployment was authorized for this review build.\n')
print('HTML',OUT/'AZURAVEL_Unclosed_Ledger_Offline.html',(OUT/'AZURAVEL_Unclosed_Ledger_Offline.html').stat().st_size)
print('ZIP',zip_path,zip_path.stat().st_size,'members',len(selected)+1)
print('manifest protected entries',len(manifest['files']))
