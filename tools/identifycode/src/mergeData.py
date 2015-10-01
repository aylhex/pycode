#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-01 23:55:38
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import json
from checkCharData import show
import pickle
import os

def GetTheJson(jsontype):
    '''
    jsontype:
    low 小写字母
    up  大写字母
    num 数字
    '''
    dict_temp = {}
    # path_json_pre='../json_zhuhai/'
    if jsontype == 'low':
        templist=xrange(26)
        char_min='a'
    if jsontype == 'up':
        templist=xrange(26)
        char_min='A'
    if jsontype == 'num':
        char_min='A'
        templist=xrange(1,10)

    for i in templist:
        try:
            if jsontype == 'num':
                c=i
            else:
                c = chr(ord(char_min) + i)
            fpath='../json_zhuhai/%s.json'%c
            f = open(fpath)
            d = json.loads(f.read())
            dict_temp[c] = d
            f.close()
        except:
            pass
        
    for char in dict_temp:
        print '====== %s ======'%char
        show('_'+char)
        

result = {}
result.update(a)
result.update(A)
result.update(N)
for key in  result:
    result[key].pop('x_min')
    result[key].pop('y_min')
    result[key].pop('x_max')
    result[key].pop('y_max')
# print result
with open('data.json','wb') as f:
    f.write(json.dumps(result))