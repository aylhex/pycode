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
    def _MyDeco(*args, **kwargs):
        result = {
            "version": 1,
            "Author": "nw",
            "data": func(*args, **kwargs),
        }
        print result
        return result
    return _MyDeco


@MyDeco1
def MyFunc(a, b):
    result = {
        "errcode": 2,
        "msg": "success",
        "sum": a+b,
    }
    print result
    return result


def main():
    a,b=5,88
    print "--------------"
    MyFunc(a, b)
    print "--------------"
    MyFunc(a, b)

if __name__ == '__main__':
    main()
