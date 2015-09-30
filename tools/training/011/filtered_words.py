#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-08 22:44:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
则打印出 Freedom，否则打印出 Human Rights。
"""

def gettxtwords(fpath):
    wordlist = []
    with open(fpath, 'r') as fp:
        for i in fp.readlines():
            i=unicode(i,'utf-8')
            wordlist.append(i.strip())
    return wordlist


def iswordinthelist(strword, wordlist):
    return strword in wordlist


def main():
    fpath = r'filtered_words.txt'
    wordlist = gettxtwords(fpath)
    # print '\n'.join(wordlist)
    while True:
        try:
            strword = raw_input('>>')
            strword=unicode(strword,'gbk')
        except KeyboardInterrupt, e:
            break
        result = iswordinthelist(strword, wordlist)
        if result:
            print 'ok'
        else:
            print 'error'

if __name__ == '__main__':
    main()
