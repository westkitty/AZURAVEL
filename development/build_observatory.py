"""Deterministically embed the authoritative AZ1 dictionary and observatory sources into one offline HTML entrypoint."""
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parent.parent
TEMPLATE=(ROOT/'development/observatory_template.html').read_text(encoding='utf-8')
CSS=(ROOT/'development/observatory.css').read_text(encoding='utf-8')
JS=(ROOT/'development/observatory.js').read_text(encoding='utf-8')
DATA=json.loads((ROOT/'AZURAVEL_DATA.json').read_text(encoding='utf-8'))
assert len(DATA['entries'])==100 and all(len(e['forms'])==6 for e in DATA['entries'])
raw=json.dumps(DATA,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
for field,value in [('__OBSERVATORY_CSS__',CSS),('__AZURAVEL_JSON__',raw),('__OBSERVATORY_JS__',JS)]:
    assert TEMPLATE.count(field)==1,field
    TEMPLATE=TEMPLATE.replace(field,value)
assert not any(x in TEMPLATE for x in ['__OBSERVATORY_CSS__','__OBSERVATORY_JS__','__AZURAVEL_JSON__'])
DEST=ROOT/'index.html'
DEST.write_text(TEMPLATE,encoding='utf-8')
print('Built',DEST,'bytes',DEST.stat().st_size,'sha256',hashlib.sha256(DEST.read_bytes()).hexdigest())
