#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/12/12

import sys
import os

txtpath=r'filelist.txt'
fp=open(txtpath,'a')
#----------------------------------------------------------------------
def main(rootpath):
    """"""
    filelist=[]
    fileinfolist=[]
    #filespath=[os.path.join(rootpath,fpath.replace('/','\\').replace('\n','')) for fpath in filelist]
    for root,dirs,files in os.walk(rootpath):
        for f in files:
            fpath=os.path.join(root,f)
            filelist.append(fpath)
    fileinfolist=[(os.path.getsize(f),f.replace(rootpath+os.sep,'')) for f in filelist]
    return fileinfolist

if __name__=='__main__':
    if len(sys.argv)==2:
        rootpath=sys.argv[1]
    fileinfolist=main(rootpath)
    for s,f in fileinfolist:
        fp.write('%s  %d\n' %(f,s))
        #print '%s  %d' %(f,s)
    fp.close()