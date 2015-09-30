#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/8/11

import json
filepath=r'e:\kuaipan\study\code\python\web\vm\vmlist.json'
fp=file(filepath)
flines=fp.read()
fjson=json.loads(flines)
print fjson
print fjson[0]['name']