#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-09 13:54:02
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

"""
python 装饰器学习
"""

import os


def MyDeco1(func):
	def _MyDeco():
	    print "before MyFunc called!"
	    func()
	    print "after MyFunc called!"
	return _MyDeco


@MyDeco1
def MyFunc():
    print "MyFunc called!"


def main():
	print "--------------"
	MyFunc()
	print "--------------"
	MyFunc()

if __name__ == '__main__':
    main()
