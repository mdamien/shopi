import urllib.request, json
f = urllib.request.urlopen("http://commercesdepont.fr/json/").read().decode("utf8")
i,j = f.find("[{"),f.find("}]")
f = f[i:j+2]
f = f.replace('\n','\\n')
shops = json.loads(f)
open("scripts/shops.json","w").write(json.dumps(shops, indent=4))
