#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-14 16:38:42
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import logging
import logging.config


# 日志模块

def main():
    logging.config.fileConfig("logcfg.ini")
    LOGA = logging.getLogger("loggerrota")
    LOGA.info("info logs")

class MyLogger(object):

    """docstring for MyLogging"""

    def __init__(self,loggername, fhlevel=None, chlevel=None, maxlogsize=None):
        self.loggername = loggername
        self.logfilename = loggername
        self.logpath = ''
        if maxlogsize:
            self.maxlogsize = maxlogsize
        else:
            self.maxlogsize = 5*1024*1024
        if fhlevel:
            if fhlevel == 0:
                self.fhlevel = logging.DEBUG
            elif fhlevel == 1:
                self.fhlevel = logging.INFO
            elif fhlevel == 2:
                self.fhlevel = logging.WARN
        else:
            self.fhlevel = logging.DEBUG
        if chlevel:
            if chlevel == 0:
                self.chlevel = logging.DEBUG
            elif chlevel == 1:
                self.chlevel = logging.INFO
            elif chlevel == 2:
                self.chlevel = logging.WARN
        else:
            self.chlevel = logging.INFO

    def Logger(self):
        # 创建一个logger
        logger = logging.getLogger(self.loggername)
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.GetLogPath())
        # fh =logging.handlers.RotatingFileHandler(self.GetLogPath(), maxBytes=5*1024*1024,backupCount=5)
        fh.setLevel(self.fhlevel)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(self.chlevel)

        # 定义handler的输出格式
        fhformatter = logging.Formatter(
            '%(asctime)s-%(name)s-%(levelname)s-%(message)s', '%Y-%m-%d %H:%M:%S')
        chformatter = logging.Formatter(
            '%(asctime)s-%(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(fhformatter)
        ch.setFormatter(chformatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    def GetLogPath(self):
        fpath = os.path.realpath(__file__)
        fdirpath, basename = os.path.split(fpath)
        logpath = os.path.join(fdirpath, 'log')
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        logpath = os.path.join(logpath, self.logfilename+'.log')
        self.FormatLogPath(logpath)
        self.logpath = logpath
        return logpath

    def FormatLogPath(self, logpath):
        renamelogpath = logpath+'0'
        if not os.path.exists(logpath):return True
        if os.path.getsize(logpath) >= self.maxlogsize:
            try:
                os.remove(renamelogpath)
            except WindowsError, e:
                raise e
            os.rename(logpath, renamelogpath)
            return True


def TestMyLogger():
    lg = MyLogger(__name__)
    LOGA = lg.Logger()
    for i in range(10000):
        LOGA.info('logging file')

if __name__ == '__main__':
    main()
