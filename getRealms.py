import requests as rq
import json
import io
apikey = "apikey=ks3xtugk5fdjdvp45h9yyq7756jszzg2"
URL = ".api.battle.net/wow/realm/status?locale=en_US&"
URL2 = ".api.battle.net/wow/auction/data/"
realmDict = {
	"us":[],
	"tw":[],
	"kr":[],
	"eu":[]}
#I found locale actually affects nothing but only its language
#so never mind and let us use only english

for i in realmDict.keys():
	print("currently running : "+i)
	uri = "https://"+i+URL+apikey
	try:
		res = rq.get(uri)
	except:
		print("failed:"+uri)
		break
	if res.status_code!=200:
		print("failed:"+uri)
		break
	try:
		js = res.json()
	except:
		print("failed:"+uri)
		break
	for j in js['realms']:
		name = j['name']
		uri2 = "https://"+i+URL2+name+"?"+apikey
		res2 = rq.get(uri2)
		js2 = res2.json()
		AH = js2['files'][0]['url']
		dic = {name:AH}
		realmDict[i].append(dic)
st = json.dumps(realmDict)
with open("realms","w") as f:
	f.write(st)
