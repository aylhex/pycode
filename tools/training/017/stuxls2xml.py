#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-18 22:06:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>


PS:
调试过程遇到编码坑…（叫做python2坑更合适）

列表和字典转换为字符串无法原生地表现出其中 utf-8 编码的效果并写入文件（print都显示不出对应的效果）

被这几个题弄得神烦，感觉花费了太多时间了

>>> str(l)
"['\\xe4\\xbd\\xa0\\xe5\\xa5\\xbd', 2]"
看到了转义，尝试使用raw字符串解决问题

后来想到了变量和格式化的方法,也都无法解决问题

顺便感觉中文编码真心万恶。。。英文直接就可以用了

原来我不是一个人，python中文字符转义问题

要不是python2安装库比较方便，现在绝对立马换python3了

这周之后了解下python2和python3共存，并且在python2主系统环境下安装各种python3库的方法吧

关于如何实现带中文字符串的list或者dict直接转化为对应的字符串，不进行转义修饰，请教下前辈

"""

import xlrd
from lxml import etree
import simplejson as json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def readxls(fpath):
    strjson = {}
    w = xlrd.open_workbook(fpath)
    wsheet = w.sheet_by_index(0)
    rows = wsheet.nrows
    for i in range(rows):
        vlist = wsheet.row_values(i)
        for j in range(len(vlist)):
            if type(vlist[j]) == float:
                vlist[j] = int(vlist[j])
        strjson[vlist[0]] = vlist[1:]
    strjson = json.dumps(strjson)
    return strjson


def creatxml(strjson):
    # strxml=u"""<?xml version="1.0" encoding="UTF-8"?>"""
    root = etree.Element(u'root')
    students = etree.SubElement(root, u'students')
    comm = etree.Comment(u"""
        学生信息表 
        "id" : [名字, 数学, 语文, 英文]
        """)
    students.append(comm)
    students.text = str(strjson)
    tree = etree.ElementTree(root)
    tree.write("students.xml", pretty_print=True,
               xml_declaration=True, encoding='utf-8')


def main():
    fpath = u'students.xls'
    strjson = readxls(fpath)
    # print type(strjson)
    creatxml(strjson)
    print 'ok'

if __name__ == '__main__':
    main()
