#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 13:49:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</citys>
</root>
"""


import xlrd
import simplejson as json
from lxml import etree

def readxls(fpath):
    strjson={}
    w=xlrd.open_workbook(fpath)
    ws=w.sheet_by_index(0)
    nrows=ws.nrows
    for row in range(nrows):
        rowdata=ws.row_values(row)
        strjson[rowdata[0]]=rowdata[1]
    return strjson

def createxml(strjson):
    root=etree.Element(u'root')
    citys=etree.SubElement(root,'citys')
    comm=etree.Comment(u"""城市信息""")
    citys.append(comm)
    citys.text=str(strjson)
    tree=etree.ElementTree(root)
    tree.write(u'citys.xml',pretty_print=True,xml_declaration=True,encoding='utf-8')
def main():
    fpath = u'citys.xls'
    strjson = readxls(fpath)
    # print strjson
    createxml(strjson)
    print 'ok'

if __name__ == '__main__':
    main()
