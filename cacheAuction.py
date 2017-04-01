import requests as rq
import time
import json
import sys

setregion="none"
if len(sys.argv)==2:
	setregion = sys.argv[1]
	print("set region : "+setregion)

f=open("realms","r")
s=f.read()
f.close()
js=json.loads(s)
keys=list(js.keys())
keys.sort()

def CacheOne(i):
	for j in js[i]:
		name=list(j.keys())[0]
		print("saving : "+i+" - "+name+"...")
		AH=j[name]
		try:
			res = rq.get(AH)
		except:
			print("failed!!!")
			continue
		updatetime = int(time.time())
		title = "data/"+i+"_"+name+"_"+str(updatetime)+".txt"
		with open(title,"w") as f:
			f.write(res.text)

while True:
	t1 = time.time()
	if setregion in keys:
		CacheOne(setregion)
	else:
		for i in keys:
			CacheOne(i)
	t2 = time.time()
	dt = t2 - t1
	wt = 3600.0-dt
	print(str(dt)+"elapsed...")
	print("waiting for the next period...")
	if wt>0:
		time.sleep(wt)
