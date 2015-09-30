#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-08 22:44:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import re

"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""


def gettxtwords(fpath):
    wordlist = []
    with open(fpath, 'r') as fp:
        for i in fp.readlines():
            i = unicode(i, 'utf-8')
            wordlist.append(i.strip())
    return wordlist


def getpattern(wordlist):
    return '|'.join(wordlist)


def getresultstring(strpattern):
    while True:
        try:
            strword = raw_input('>>')
            strword = unicode(strword, 'gbk')
        except KeyboardInterrupt, e:
            break
        result = re.sub(strpattern, '**', strword)
        print result


def main():
    fpath = u'filtered_words.txt'
    wordlist = gettxtwords(fpath)
    strpattern = getpattern(wordlist)
    getresultstring(strpattern)

if __name__ == '__main__':
    main()
