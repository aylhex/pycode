#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-28 10:54:40
# @Author  : cj (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
返回值：
返回一个元组 (代码行数,注释行数,空白行数)
"""

import os
import re
from itertools import imap

codenum = 0
notenum = 0
blanknum = 0
t_code = 1
t_note = 2
t_blank = 3


def getFileList(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            fpath = os.path.join(root, f)
            if os.path.splitext(fpath)[1] == r'.py':
	        	yield fpath


def getlinesfromtxt(filepath):
    try:
        with open(filepath,'r') as fp:
            return True, fp.readlines()
    except WindowsError, e:
        return False, e


def getTheLineType(strline):
	
	if strline.find('#')!=-1:
		return t_note
	elif re.match(r'^\s*$', strline):
		return t_blank
	else:
		return t_code
def everyfile(filepath):
	codenum_tmp=0
	notenum_tmp=0
	blanknum_tmp=0
	result,strlines=getlinesfromtxt(filepath)
	if not result:
		print 'cannot read the file'
	else:
		for line in strlines:
			t_type=getTheLineType(line)
			if t_type==t_blank:
				blanknum_tmp+=1
			elif t_type==t_note:
				notenum_tmp+=1
			else:
				codenum_tmp+=1
	return (codenum_tmp,notenum_tmp,blanknum_tmp)

def adder(x,y):
	return (x[0]+y[0],x[1]+y[1],x[2]+y[2])

def main():
    # dirpath=r'x:\study\code\python'
    dirpath=r'e:\kuaipan\study\code\python\tools\kcloudpop'
    filelist=getFileList(dirpath)
    countlist=imap(everyfile,filelist)
    codenum,notenum,blanknum=reduce(adder, countlist)
    return (codenum,notenum,blanknum)

if __name__ == '__main__':
    print main()
