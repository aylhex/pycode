#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import sys
import filecmp

def main(path1,path2):
    result=filecmp.dircmp(path1,path2)
    print result.left_only
    print result.same_files
    print result.diff_files
    result.report_full_closure()
if __name__=='__main__':
    path1=r'e:\temp\1'
    path2=r'e:\temp\2'
    main(path1,path2)