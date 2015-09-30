#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
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