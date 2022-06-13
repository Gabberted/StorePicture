import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")

import dbConn as db

import urllib.request

strQ="select count(*) from pictures"
strCount=str(db.returnFetchall(strQ)[0]).split(",")[0].replace("(","")
print(strCount)
if strCount=="0":
    strCount=1
else:
    strCount=str(int(strCount)+1)

page = urllib.request.urlopen('http.cat/' + str(strCount))
btext=page.read()
print(btext)