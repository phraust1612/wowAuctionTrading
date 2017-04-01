import requests as rq
import time
import json

f=open("realms","r")
s=f.read()
f.close()
js=json.loads(s)
keys=list(js.keys())

def CacheOne():
	for i in keys:
		for j in js[i]:
			name=list(j.keys())[0]
			AH=j[name]
    		try :
        		res = rq.get(AH)
    		except:
				continue
			updatetime = time.time()
    		title = i+"_"+name+"_"+str(updatetime)+".txt"
    		f = open(title,"w")
    		f.write(res.text)
    		f.close()

while True:
    CacheOne()
    time.sleep(3600)
