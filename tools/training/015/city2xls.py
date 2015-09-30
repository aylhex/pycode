#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-18 20:21:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}

请将上述内容写到 city.xls 文件中，如下图所示：
"""


import os
import simplejson as json
import xlwt

def readtxt(fpath):
    with open(fpath,'r') as fp:
        strtxt=fp.read(8000)
        return unicode(strtxt,'utf-8')

def getjsonfromstr(strtxt):
    strdict=json.loads(strtxt)
    strdict=sorted(strdict.iteritems(),key=lambda x:x[0])
    return strdict

def writexls(strdict):
    wp=xlwt.Workbook()
    ws=wp.add_sheet('citys')
    count=len(strdict)
    for row in range(count):
        ws.write(row,0,strdict[row][0])
        ws.write(row,1,strdict[row][1])
    wp.save('citys.xls')

def main():
    fpath=u'city.txt'
    strtxt=readtxt(fpath)
    strdict=getjsonfromstr(strtxt)
    writexls(strdict)
    print 'ok'

if __name__ == '__main__':
    main()