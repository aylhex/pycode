#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 16:31:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
    数字信息
-->

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]

</numbers>
</root>

"""

import simplejson as json
from lxml import etree
import xlrd

def readxls(fpath):
    strjson=[]
    w=xlrd.open_workbook(fpath)
    ws=w.sheet_by_index(0)
    nrows=ws.nrows
    for row in range(nrows):
        temp=ws.row_values(row)
        rlist=[int(item) for item in temp if type(item)==float]
        strjson.append(rlist)
    return strjson

def createxml(strjson):
    root=etree.Element(u'root')
    mynumbers=etree.SubElement(root,u'numbers')
    comm=etree.Comment(u"""数字信息""")
    mynumbers.append(comm)
    mynumbers.text=str(strjson)
    tree=etree.ElementTree(root)
    tree.write(u'numbers.xml',pretty_print=True,xml_declaration=True,encoding='utf-8')

def main():
    fpath=u'numbers.xls'
    strjson=readxls(fpath)
    createxml(strjson)
    print 'ok'

if __name__ == '__main__':
    main()