#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-30 14:08:24
# @Author  : cj (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

import os
import sys
from bs4 import BeautifulSoup

def parseHtml(strhtml):
	soup=BeautifulSoup(strhtml)
	return soup.h4.string

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    pathhtml=r'test.html'
    result=parseHtml(open(pathhtml).read())
    print result

if __name__ == '__main__':
    main()
