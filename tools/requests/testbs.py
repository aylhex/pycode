#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-20 15:20:59
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : http://www.ijinshan.com
# @Version : $Id$

import bs4
def main():
    fp=open(r'e:\kuaipan\study\code\python\tools\requests\test.html','r')
    strhtml=fp.read()
    fp.close()
    bsobj=bs4.BeautifulSoup(strhtml)
    select=bsobj.find('select',{'class':'chosen-select dy-chosen'})
    print select

if __name__ == '__main__':
    main()
