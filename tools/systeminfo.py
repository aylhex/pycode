#!/usr/bin/env python
#coding:utf-8
# Author:   --<chenjun>
# Purpose: 
# Created: 2014/6/14

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