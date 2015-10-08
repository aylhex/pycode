#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-08 20:13:55
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import sys
import requests
import arrow
import time

DOWNURL=r'http://wx.zhcgs.gov.cn/ValidateCodeHeper'
PATHFORSAVE=os.path.abspath('../tmp/')

def initDir():
    if not os.path.exists(PATHFORSAVE):
        os.mkdir(PATHFORSAVE)
def GetPicSavePath(picname):
    picname = str(picname)+'.jpg'
    PicPath=os.path.join(PATHFORSAVE,picname)
    return PicPath

def HttpDownload():
    result=False
    picname = arrow.now().timestamp
    PicPath=GetPicSavePath(picname)
    r=requests.get(DOWNURL)
    with open(PicPath,'wb') as fp:
        fp.write(r.content)
    result=True
    return result

def DownLoadPic(picnum):
    for i in range(picnum):
        print "download img: %d" %i
        HttpDownload()
        print "sleep 1000 ms"
        time.sleep(1) 
    print "over!!!"

def main():
    if len(sys.argv) == 2:
        picnum=int(sys.argv[1])
    else:
        picnum=10
    initDir()
    DownLoadPic(picnum)

if __name__ == '__main__':
    main()