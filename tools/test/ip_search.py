#!/usr/bin/env python
#coding:utf-8
# Author:   --<cj>
# Purpose: 
# Created: 2013/11/11

import sys
import urllib2,re
#http://www.ip138.com/ips138.asp?ip=113.106.106.131&action=2
#http://iframe.ip138.com/ic.asp
ip_self_url=r'http://iframe.ip138.com/ic.asp'
ip_search_url=r'http://www.ip138.com/ips138.asp'
re_self_strs='<center>(.*)</center>'
re_search_strs='<td align="center"><ul class="ul1"><li>(.*)</li><li>'
def get_selfip():
    try:
        self_data=urllib2.urlopen(ip_self_url).read(1000)
        ip=re.findall(re_self_strs,self_data)
        return ip[0]
    except:
        return 'IANA'
def searchIP(ip):
    try:
        search_url=ip_search_url+'?ip=%s&action=2'%ip
        search_data=urllib2.urlopen(search_url).read(10000) 
        ip=re.findall(re_search_strs,search_data)
        return ip[0]
    except:
        return 'IANA'
if __name__=='__main__':
    if len(sys.argv)>=2:
        ip=sys.argv[1]
    else:
        ip='0.0.0.0'
    selfip=get_selfip()
    print selfip
    print r'search->>%s'%ip
    print searchIP(ip)