import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")

import dbConn as db

import urllib.request

def QueryURL(url):
    strCount="1"
    try:
        page = urllib.request.urlopen(url)
        btext=page.read()
        print(btext)
    except Exception as ex:
        print(f"Error: {ex}")
        strCount=str(int(strCount)+1)
        url="https://http.cat/" + str(strCount)
        QueryURL(url)


strQ="select count(*) from pictures"
strCount=str(db.returnFetchall(strQ)[0]).split(",")[0].replace("(","")
print(strCount)
if strCount=="0":
    strCount=1
else:
    strCount=str(int(strCount)+1)

url="https://http.cat/" + str(strCount)
print(f"Probing url:{url}")
QueryURL(url)


