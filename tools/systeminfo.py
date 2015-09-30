#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import sys
import unittest
import platform

#----------------------------------------------------------------------
def geisysteminfo():
    """"""
    print platform.system()
    print platform.version()
    print platform.architecture()
    print platform.node()
    print platform.java_ver()
    print platform.dist()
    print platform.python_version()
    print platform.win32_ver()

if __name__=='__main__':
    geisysteminfo()
    #platform.system()
    unittest.main()