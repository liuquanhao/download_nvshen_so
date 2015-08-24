#!/usr/bin/python

import urllib2
import sys,os
from urllib2 import HTTPError

import threading

baseUrl = "http://www.nvshen.so/wp-content/uploads/2015/"
#baseUrl = "http://www.nvshen.so/wp-content/uploads/2014/"
basePath ="/tmp/vnshen_so/"
threads = []

if(os.path.exists(basePath) == False):
    os.mkdir(basePath)

def downloadImage(url,localPath):
    try:
        request = urllib2.Request(url)
        request.add_header("User-Agent","fake-client")
        response = urllib2.urlopen(request)
        f = file(localPath,"wb")
        f.write(response.read())
        f.close()
    except HTTPError:
        pass
        
def getLocalPath(mon):
    childPath = basePath + mon
    if(os.path.exists(childPath) == False):
        os.mkdir(childPath)
    return childPath

def getUrlPath(mon):
    childUrl = baseUrl + mon
    return childUrl

def download(tmpPath,tmpUrl):
    for img in range(1,1300):
        localPath = tmpPath + str(img) + ".jpg"
        if(os.path.exists(localPath)):
           continue
        print(localPath)
        url = tmpUrl + str(img) + ".jpg"
        downloadImage(url,localPath)

def startDownload():
    for pt in ("01/","02/","03/","04/","05/","06/","07/","08/"):
    #for pt in ("12/",):
        tmpPath = getLocalPath(pt)
        tmpUrl = getUrlPath(pt)
        thr = threading.Thread(target=download,args=(tmpPath,tmpUrl))
        threads.append(thr)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    startDownload()
    
