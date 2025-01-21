import urllib.request
import json

with open('assessments.json','r',encoding='utf-8') as f:
    j=json.load(f)
for s in j[0]['slides']:
    urllib.request.urlretrieve(s['images'][-1]['url'],s['caption']+'.jpg')