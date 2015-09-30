#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-28 00:22:40
# @Author  : cj (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os
import glob2
import re
import itertools


def getLogList(dirpath):
    logpath = os.path.join(dirpath, 'log') + '\\*.txt'
    loglist = glob2.iglob(logpath)
    for log in loglist:
        yield log


def getwordsfromtxt(logpath):
    try:
        with open(logpath,'r') as fp:
            return True, fp.read()
    except WindowsError, e:
        return False, e


def getKeyWord(words):
    dirctWord = {}
    wordlist = re.findall(r'\b(\w+\'?\w+)\b', words)
    for item in wordlist:
        if item not in dirctWord.keys():
            dirctWord[item] = 1
        else:
            dirctWord[item] += 1
    worddirct = {dirctWord[item]: item for item in dirctWord.keys()}
    maxnum = max(worddirct.keys())
    # print worddirct[maxnum], maxnum
    return worddirct[maxnum], maxnum


def main():
    dirpath = os.path.dirname(__file__)
    loglist = getLogList(dirpath)
    keywords = {}
    for log in loglist:
        # print log
        result, words = getwordsfromtxt(log)
        if result:
            keyword,keynum = getKeyWord(words)
        else:
            keyword = 'Null'
            keynum=0
        keywords[os.path.basename(log)]=keyword+' '+str(keynum)
    keywords_new=sorted(keywords.items(),key=lambda x:x[0])
    for k,v in keywords_new:
    	print k,v

if __name__ == '__main__':
    main()
