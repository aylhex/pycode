#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-01-07 15:37:53
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : www.ijinshan.com
# @Version : $Id$

import requests
import os

def TestWh():
	strUrl = r"http://rq.wh.cmcm.com/res/"
	data = {
		    "city_id": "101280701", 
		    "coexist_product": 80, 
		    "default_browser": 5, 
		    "enable_pushmsg": 1, 
		    "ie_version": "0b00280040db", 
		    "install_time": 1447035079, 
		    "product_ver": 1535010710, 
		    "scene_list": [
		        {
		            "id": 1, 
		            "match_info": "", 
		            "scene_ver": 1
		        }, 
		        {
		            "id": 2, 
		            "match_info": "8", 
		            "scene_ver": 1
		        }, 
		        {
		            "id": 3, 
		            "match_info": "11", 
		            "scene_ver": 1
		        }, 
		        {
		            "id": 4, 
		            "match_info": "10|11", 
		            "scene_ver": 1
		        }, 
		        {
		            "id": 5, 
		            "match_info": "15|17", 
		            "scene_ver": 1
		        }
		    ], 
		    "system_ar": 32, 
		    "system_ver": "1201", 
		    "tid": "100-50", 
		    "tod": "100-50", 
		    "tryno": "1337", 
		    "user_tag": "9901", 
		    "uuid": "BF64F2E9886E8F51A41457F1FDB43F26"
		}
	response = requests.post(strUrl,data=data)
	# strJson = response.json()
	print response.status_code
	print response.text

def main():
	TestWh()

if __name__ == '__main__':
	main()