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
    logging.basicConfig(filename=GetScriptName(),level=logging.INFO,format='%(asctime)s %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    return logger

def loggerNew():
    # 创建一个logger  
    logger = logging.getLogger('mylogger')  
    logger.setLevel(logging.DEBUG)  
      
    # 创建一个handler，用于写入日志文件  
    fh = logging.FileHandler(GetScriptName())  
    fh.setLevel(logging.DEBUG)
      
    # 再创建一个handler，用于输出到控制台  
    ch = logging.StreamHandler()  
    ch.setLevel(logging.INFO)  
      
    # 定义handler的输出格式  
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')  
    fh.setFormatter(formatter)  
    ch.setFormatter(formatter)  

    # 给logger添加handler  
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def GetScriptName():
    fpath=os.path.realpath(__file__)
    fdirpath,basename=os.path.split(fpath)
    logpath=os.path.join(fdirpath,'log')
    if not os.path.exists(logpath):
        os.mkdir(logpath)
    logpath=os.path.join(logpath,os.path.splitext(basename)[0]+'.log')
    return logpath

def main():
    LOGA=loggerNew()
    LOGA.debug('logging file')

if __name__ == '__main__':
    main()