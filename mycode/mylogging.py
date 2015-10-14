#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-14 16:38:42
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import logging

#日志模块
def logger():
    """"""
    logger=logging.getLogger()
    # logger.setLevel(logging.INFO)
    # fh=logging.FileHandler(GetScriptName(),'a')
    # fh.setLevel(logging.DEBUG)
    # fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    # fh.setFormatter(fm)
    # logger.addHandler(fh)
    logging.basicConfig(filename=GetScriptName(),level=logging.INFO,format='%(asctime)s %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    return logger

def GetScriptName():
    fpath=os.path.realpath(__file__)
    basename=os.path.basename(fpath)
    sname=os.path.splitext(basename)[0]+'.log'
    return sname

def main():
    LOGA=logger()
    LOGA.info('logging file')

if __name__ == '__main__':
    main()