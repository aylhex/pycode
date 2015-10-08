#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-03 18:12:07
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import sys
from identify import GETSTAND

def autostudy(fpath):
    result=False
    # fpath='../pic/17380.jpg'
    if not os.path.exists(fpath):
        return result
    result = GETSTAND(fpath)
    return result

def WalkThePics(dir_pic):
    result=False
    err_files=[]
    if not os.path.exists(dir_pic):
        return result,err_files.append("the dir is not exists")
    for root,dirs,files in os.walk(dir_pic):
        for f in files:
            fpath = os.path.join(root,f)
            result = autostudy(fpath)
            if not result:
                err_files.append(fpath)
    if not err_files:
        result = True
    else:
        result = False
    return result,err_files

def main():
    if len(sys.argv)==2:
        fpath=sys.argv[1]
        result = autostudy(fpath)
        print result
    else:
        dir_pic=r'../pic/'
        result,err_files = WalkThePics(dir_pic)
        print "result:",result
        print "msg:"
        for i in err_files:
            print i

if __name__ == '__main__':
    main()
