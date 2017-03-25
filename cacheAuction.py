import requests as rq
import time

AH = "http://auction-api-kr.worldofwarcraft.com/auction-data/b5379d0559a34568a129fea645c060b9/auctions.json"
LM = "https://kr.api.battle.net/wow/auction/data/durotan?locale=ko_KR&apikey=ks3xtugk5fdjdvp45h9yyq7756jszzg2"

def LastModified():
    global AH
    ans = int(time.time())
    try:
        res = rq.get(LM)
    except requests.exceptions.ConnectionError:
        return ans
    if res.status_code != 200:
        return ans
    js = res.json()
    ans = js['files'][0]['lastModified']
    ans /= 1000
    checkurl = js['files'][0]['url']
    if checkurl != AH:
        AH = checkurl
    return ans
        
def CacheOne():
    updatetime = LastModified()
    try :
        res = rq.get(AH)
    except:
        return -1
    title = str(updatetime)+".txt"
    f = open(title,"w")
    f.write(res.text)
    f.close()
    return 0

while True:
    tmp = SaveOne()
    while tmp!=0:
        tmp = SaveOne()
    time.sleep(1800)
