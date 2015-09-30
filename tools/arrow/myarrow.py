#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
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