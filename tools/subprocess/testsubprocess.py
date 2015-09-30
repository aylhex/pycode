#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-05-01 10:40:04
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : www.ijinshan.com
# @Version : $Id$

import subprocess

def test():
    p=subprocess.Popen(r"test.bat", shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutput,erroutput = p.communicate() 
    print stdoutput
    # print erroutput
def main():
    test()

if __name__ == '__main__':
    main()