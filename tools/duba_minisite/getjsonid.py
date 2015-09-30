#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-28 11:55:50
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : http://www.ijinshan.com
# @Version : $Id$
"""
本脚本用途:
获取外网新闻的jsonid

用法:
支持一个参数，此参数即为频道号，
若传递的频道名不合法，则按default处理
例：
getjsonid.py 1335
getjsonid.py 3948

或者不传任何参数，脚本将遍历所有频道的jsonid

频道说明:
channellist=['1335','1509','1337','1338','1339',]
其中结果中会有root、default两个频道
root   http://hotnews.duba.com/data/json/HotNews.json
default  http://hotnews.duba.com/minisite/default/data/json/HotNews.json

"""


import requests
import simplejson
import sys

channellist=['1335','1509','1337','1338','1339',]

def getjson(strurl):
    # 下载json数据，设置超时20s
    try:
        strhtml=requests.get(strurl,timeout=20).text
    except requests.exceptions.RequestException.timeout, e:
        strhtml=None
    if strhtml:
        strjson=simplejson.loads(strhtml)
    else:
        strjson=None
    return strjson

def parsejsonid(strjson):
    if not strjson:
        return 'None'
    strid=strjson.get('id','')
    return strid
def getsinglejsonid(strchannel):
    """
    http://hotnews.duba.com/data/json/HotNews.json
    http://hotnews.duba.com/minisite/1339/data/json/HotNews.json
    http://hotnews.duba.com/minisite/default/data/json/HotNews.json

    """
    if strchannel not in channellist:
        strchannel='default'
    jsonurl=u'http://hotnews.duba.com/minisite/%s/data/json/HotNews.json' %strchannel
    if strchannel=='root':
        jsonurl=u'http://hotnews.duba.com/data/json/HotNews.json'
    strjson=getjson(jsonurl)
    jsonid=parsejsonid(strjson)
    return jsonid

def getallchanneljsonid():
    jsonid_dict={}
    jsonid_dict['default']=getsinglejsonid('default')
    jsonid_dict['root']=getsinglejsonid('root')
    for item in channellist:
        jsonid_dict[item]=getsinglejsonid(item)
    return jsonid_dict

def main():
    if len(sys.argv)==1:
        jsonid_dict=getallchanneljsonid()
        for item in jsonid_dict.keys():
            print '%s jsonid: %s'%(item,jsonid_dict[item])
    else:
        strchannel=sys.argv[1]
        jsonid=getsinglejsonid(strchannel)
        print '%s jsonid: %s' %(strchannel,jsonid)

if __name__ == '__main__':
    main()