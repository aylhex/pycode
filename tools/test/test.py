#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/8/19

import urllib
import base64
import json
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
第一步把\n替换掉
第二步把\" 替换成 "
第三步正则匹配
re.findall(r'class"WB_text[\s\S]+?nick-name="金山食堂"\>([\s\S]+?)<',a)
"""

def main():
    # strhtml=open(r'e:\svn\sae\weixincmcm\1\test2.html','r').read()
    strhtml=open(r'e:\SVN\sae\weixincmcm\1\test.html','r').read()
    strhtml=strhtml.decode('gbk').encode('utf-8')
    format_html={
        r'\t':'',
        r'\n':'',
        r'\r':'',
        '\\':'',
    }
    for k,v in format_html.items():
        # print k,v
        strhtml=strhtml.replace(k,v)
    # print strhtml
    sss=re.findall(r'class="WB_text[\s\S]+?nick-name="金山食堂">([\s\S]+?)<',strhtml)
    i=0
    for item in sss:
        item=item.strip()
        print i,item
        i+=1
if __name__ == '__main__':
    main()