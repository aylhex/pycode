#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/1/23
import sys,os
import urllib,json
kwifiurl=r'http://wifi.liebao.cn/hd/214/port.php?id='
setstrs=r'quit ==>to exit the exe'
#----------------------------------------------------------------------
def getinfo(appid):
    """"""
    urls=kwifiurl+str(appid)
    s=urllib.urlopen(urls)
    try:
        wifi_json=s.read()
        wifi_strs=json.loads(wifi_json)
    except:
        wifi_strs={}
    #everystrs='--------'+'\n'+'id='+str(appid)+'\n'
    print '-'*10
    if wifi_strs.has_key('wish') and wifi_strs['wish']:
        print 'ID='+str(appid)
        for i in wifi_strs.keys():
            print i,wifi_strs[i]
            #everystrs+=str(i)+repr(wifi_strs[i])+'\n'
    else:
        print '%d is not exists!'%appid
    print '-'*10
    os.system('pause')
    #logger.writelines(everystrs)
if __name__=='__main__':
    #logpath=os.path.join(sys.path[0],'mystrs.txt')
    #logger=open(logpath,'w+')
    while True:
        os.system('cls')
        print setstrs
        num_temp=raw_input('please input a num:')
        if num_temp=='quit':
            sys.exit()
        try:
            num=int(num_temp)
        except:
            num=2
        getinfo(num)
        #for i in xrange(1,num):
            #getinfo(i)
        
    