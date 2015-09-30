#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-12 16:41:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from xlwt import Workbook
import simplejson as json

"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
"""


def readtxt(fpath):
    with open(fpath,'r') as fp:
        strtxt=fp.read(8000)
    return unicode(strtxt,'utf-8')

def json2dirct(strjson):
    strdirct=json.loads(strjson)
    strdirct=sorted(strdirct.iteritems(),key=lambda x:x[0])
    # strdirct=dict(strdirct_sorted)
    return strdirct

def writexls(strdirct):
    w=Workbook()
    ws=w.add_sheet(u'测试',cell_overwrite_ok=True)
    for row in range(len(strdirct)):
        rowdata=strdirct[row]
        ws.write(row,0,rowdata[0])
        for col in range(1,len(rowdata[1])+1):
            ws.write(row,col,rowdata[1][col-1])
    try:
        w.save('students.xls')
        return True,'successed saved'
    except IOError, e:
        return False,e

def main():
    jsonpath=u'test.json'
    strjson=readtxt(jsonpath)
    strdirct=json2dirct(strjson)
    # print strdirct
    print writexls(strdirct)


if __name__ == '__main__':
    main()

