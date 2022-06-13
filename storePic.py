import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")

import dbConn as db

import urllib.request

strQ="select count(*) from pictures"
strCount=db.returnFetchall(strQ)[0]

if strCount=="0":
    strCount=1
else
    strCount=str(int(strCount)+1)

page = urllib.request.urlopen('http.cat/' + strCount)
btext=page.read()
print(btext)