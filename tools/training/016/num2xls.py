#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-18 20:45:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535], 
    [20, 90, 13],
    [26, 809, 1024]
]

请将上述内容写到 numbers.xls 文件中，如下图所示：
"""

import xlwt
import simplejson as json


def readtxt(fpath):
    with open(fpath, 'r') as fp:
        strtxt = fp.read(8000)
        return unicode(strtxt,'utf-8')


def getlistfromstr(strtxt):
    # 原来simplejson模块可以直接将文本中的列表直接转换成py可用的list格式，神器哈
    strjson=json.loads(strtxt)
    return strjson


def writexls(strjson):
    wp = xlwt.Workbook()
    ws = wp.add_sheet('numbers')
    for row in range(len(strjson)):
        rowdata = strjson[row]
        # print rowdata
        for col in range(len(rowdata)):
            # print rowdata[col]
            ws.write(row, col, rowdata[col])
    wp.save('numbers.xls')


def main():
    fpath = u'mynumbers.txt'
    strtxt = readtxt(fpath)
    # print strtxt
    strjson = getlistfromstr(strtxt)
    # print strjson
    writexls(strjson)
    print 'ok'

if __name__ == '__main__':
    main()
