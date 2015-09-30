#!/usr/bin/env python
# coding:utf-8
# Author:   --<chenjun>
# Purpose:
# Created: 2015/3/6

import sys
import re
#----------------------------------------------------------------------


def readwords(filepath):
    try:
        with open(filepath, 'r') as fp:
            words = fp.read()
    except WindowsError:
        print 'cannot found the textpath!'
        words = ''
    return words

#----------------------------------------------------------------------


def countwords(words):
    wordlist = re.findall(r'\b(\w+\'?\w+)\b', words)
    wordnum = len(wordlist)
    return wordnum

#----------------------------------------------------------------------


def main():
    textpath = r'test.txt'
    if len(sys.argv) > 2:
        textpath = sys.argv[1]
    words = readwords(textpath)
    wordcount = countwords(words)
    print wordcount
    return wordcount

if __name__ == '__main__':
    main()
