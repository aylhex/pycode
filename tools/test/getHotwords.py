#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/6/15

import sys
import chardet
import requests
import json

reload(sys)
sys.setdefaultencoding('utf-8')
#----------------------------------------------------------------------
def gethotword1():
    """"""
    hoturl=r'http://news.baidu.com/n?m=rddata&v=hot_word&type=0&date=&qq-pf-to=pcqq.c2c'
    strWeb=requests.get(hoturl).text
    strJson=json.loads(strWeb)
    for item in strJson['data']:
        print item.get('title','')
#----------------------------------------------------------------------
def gethotword2():
    """"""
    hoturl=r'http://dl.pop.www.duba.net/weatherpanelbg/quicknethotwords.html'
    strweb=requests.get(hoturl).text
    strweb=strweb.decode('gbk').encode('utf-8')
    strweb=strweb.split('^')
    for i in strweb:
        print i
#----------------------------------------------------------------------
def main():
    """"""
    if len(sys.argv)==2:
        num=sys.argv[1]
    else:
        num='2'
    # num='2'
    if num=='1':
        gethotword1()
    else:
        gethotword2()
if __name__=='__main__':
    main()