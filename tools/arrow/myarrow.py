#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-29 23:27:50
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : www.ijinshan.com
# @Version : $Id$

import arrow

def getmytime():
    # uttime=arrow.now()
    uttime=arrow.utcnow()
    print uttime.timestamp
    print uttime.format('YYYY-MM-DD HH:mm:ss')
    print uttime.humanize()
    print uttime.weekday()


def main():
    getmytime()

if __name__ == '__main__':
    main()