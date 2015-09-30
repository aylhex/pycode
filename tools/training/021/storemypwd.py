#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-27 14:15:21
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : http://www.ijinshan.com
# @Version : $Id$

"""
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
"""

import hashlib
from hmac import HMAC
from os import urandom

def entrcy_pwd(strpwd):
    result=hashlib.new('sha256',strpwd).hexdigest()
    return result

def entrcy_saltandpwd(strpwd,salt=None):
    if not salt:
        salt=urandom(8)
    result=entrcy_pwd(strpwd)
    result=HMAC(result,salt,hashlib.sha256).hexdigest()
    return salt,result

def main():
    strpwd='kingsoft'
    salt,result=entrcy_saltandpwd(strpwd)
    print repr(salt)
    print result

if __name__ == '__main__':
    main()