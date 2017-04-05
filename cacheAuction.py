from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import sys

f=open("realms","r")
s=f.read()
f.close()
js=json.loads(s)
keys=list(js.keys())
keys.sort()
setregion=keys
if len(sys.argv)>=2:
        setregion = sys.argv[1:]

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

def CacheOne(i):
	for j in js[i]:
                name=list(j.keys())[0]
                print("saving : "+i+" - "+name+"...")
                AH=j[name]
                driver.get(AH)
                page = driver.page_source
                soup = BeautifulSoup(page,"html.parser")
                res = soup.text
                res = res.replace("\n","")
                res = res.replace("\t","")
                resjs = json.loads(res)
                res = json.dumps(resjs)
                updatetime = int(time.time())
                title = "data/"+i+"_"+name+"_"+str(updatetime)+".txt"
                with open(title,"w") as f:
                        f.write(res)

while True:
        t1 = time.time()
        for i in setregion:
                if i in keys:
                        CacheOne(i)
        t2 = time.time()
        dt = t2 - t1
        wt = 7200.0-dt
        print(str(dt)+"elapsed...")
        print("waiting for the next period...")
        if wt>0:
                time.sleep(wt)
                
driver.quit()
