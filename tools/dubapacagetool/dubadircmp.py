#!/usr/bin/env python
#coding:utf-8
# Author:   --<cj>
# Purpose: 
# Created: 2014/9/24

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