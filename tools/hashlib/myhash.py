#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os 
import hashlib
import hmac

def entrcy_str(strpwd):
    result=hashlib.new('sha256',strpwd).hexdigest()
    return result
def gethmacstr(strpwd,salt=None):
    if not salt:
        salt=os.urandom(8)
    result=entrcy_str(strpwd)
    result=hmac.HMAC(result,salt,hashlib.sha256).hexdigest()
    return salt,result

def main():
    strpwd='kingsoft'
    salt,result=gethmacstr(strpwd)
    print repr(salt),result

if __name__ == '__main__':
    main()