#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 17:50:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
爬取精睿论坛图片
"""
import os
import requests
from bs4 import BeautifulSoup
from time import sleep


def login(strurl):
    login_url=u'http://bbs.vc52.cn/member.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.11 Safari/537.36',
        'Origin': 'http://bbs.vc52.cn',
        'Referer': 'http://bbs.vc52.cn/forum.php',
        'Host': 'bbs.vc52.cn',
    }
    login_data={u'username':u'274047',u'password':u'd34b2395b95613dd2790ce54e09670cf',u'quickforward':u'yes'}
    params={'mod':'logging','action':'login','loginsubmit':'yes','infloat':'yes','lssubmit':'yes','inajax':1}
    s = requests.Session()
    response=s.post(login_url,login_data,headers=headers,params=params)
    # print response.url
    # print response.text.encode('utf-8')
    sleep(3)
    strhtml=s.get(strurl).text
    return strhtml

def getimglist(strhtml):
    htmlobj=BeautifulSoup(strhtml)
    imglist_tmp=htmlobj.find_all('img')
    imglist_tmp=filter(ifimgok, imglist_tmp)
    imglist=[imgobj.get('src') for imgobj in imglist_tmp]
    return imglist

def ifimgok(imgobj):
    imgclass=imgobj.get('class')
    if imgclass and u'zoom' in imgclass:
        return True
    else:
        return False

def main():
    strurl=u'http://bbs.vc52.cn/thread-658497-1-1.html'
    strhtml=login(strurl)
    print strhtml
    imglist=getimglist(strhtml)
    print imglist

if __name__ == '__main__':
    main()
