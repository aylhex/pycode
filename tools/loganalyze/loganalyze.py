#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-14 19:07:58
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import os
import simplejson as json

def CreateJson():
    strJson={
        'result':False,
        'msg':'none',
        'data':{
            '01':'01',
            '02':'02',
            '03':'03',
            '04':'04',
        },
    }

    # dJson = json.dumps(strJson)
    return strJson

def main():
    print "analyze the log file"

def test():
    strjson = CreateJson()
    for k,v in strjson.items():
        print k,v

if __name__ == '__main__':
    test()