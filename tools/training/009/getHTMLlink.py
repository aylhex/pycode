#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

"""
第 0009 题：一个HTML文件，找出里面的链接
"""

import os
import sys
from bs4 import BeautifulSoup


def parseHtml(strhtml):
    links = []
    soup = BeautifulSoup(strhtml)
    for item in soup.find_all('a'):
        links.append(item.get('href'))
    return links

def main():
    pathhtml=r'test.html'
    links=parseHtml(open(pathhtml).read())
    for i in links:
        print i 
    

if __name__ == '__main__':
    main()
