#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/6/23

import sys
import os
#----------------------------------------------------------------------
def getfilelist(spath):
	""""""
	allfiles=[]
	for root,dirs,files in os.walk(spath):
		for f in files:
			fpath=os.path.join(root,f)
			fpath=fpath.replace(spath,'')
			if fpath[0]=='\\':
				fpath=fpath[1:]
			allfiles.append(fpath)
	return allfiles
#----------------------------------------------------------------------
def setxmlitem(item):
	""""""
	item='<item path="%s" />' %item
	return item

if __name__=='__main__':
	spath=r'C:\Users\chenjun\Desktop\router2'
	allfiles=getfilelist(spath) 
	items=map(setxmlitem,allfiles)
	for i in items:
		print i