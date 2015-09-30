#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

"""
本脚本功能：
登录10.20.223.57并获取第一页的数据地址

流程：
1、首先get方式获取到__hash__值
2、用第一步获取到的__hash__和帐号密码一起发送到登录页面
3、保存登录后的cookies
4、在前一步登录的情况下打开数据平台
5、从打开的页面中分析出所有的数据地址
"""

import os
import requests
from bs4 import BeautifulSoup


def testhotnews():
    strurl = u'http://hotnews.duba.com/data/json/HotNews.json'
    r = requests.get(strurl)
    strjson = r.json()
    print strjson['hotWords'][1]['title'].encode('utf-8')
    # print r.cookies


def getalldatalist(language='kav2010', version='1339', rStatus='1'):
    """
    参数解释:
    language='kav2010'   对应的频道
    version='1339'       对应的子版本
    rStatus='1'          数据状态，-1:全部 0:未发布 1:已发布 2:已过期

    """

    # 初始化requests对象
    r = requests.Session()

    # 先get一下登录页面,拿到hash值，登录时有用
    strurl = u'http://10.20.223.57'
    temphtml = r.get(strurl).text
    bsobj = BeautifulSoup(temphtml)
    strhash = bsobj.find('input', {'name': '__hash__'})['value']

    # 将登录信息post到登录地址
    strurl = u'http://10.20.223.57/access/checkuser'
    
    # 添加http头，伪装成浏览器的请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.11 Safari/537.36',
        'Origin': 'http://10.20.223.57',
        'Referer': 'http://10.20.223.57/Access/index',
        'Host': '10.20.223.57',
    }
    login_data = {
        u'username': u'chenjun',
        u'password': u'20120904',
        u'__hash__': strhash,
    }
    response = r.post(strurl, login_data, headers=headers)
    # print response.text.encode('utf-8')

    # 打开目标页面
    strurl = u'http://10.20.223.57/Access/index'
    params = {'select_language': language,
              'select_version': version, 'select_rStatus': rStatus}
    response = r.get(strurl, params=params)
    temphtml = response.text.encode('utf-8')
    # 从返回的html中分析出数据路径
    bsobj = BeautifulSoup(temphtml)
    rowlist = bsobj.find_all('tr')
    datalist = [row.get('data-ftp_dir')
                for row in rowlist if row.get('data-ftp_dir')]
    return datalist


def main():
    datalist = getalldatalist('kxe_com', '1339', '1')
    for i in datalist:
        print i


if __name__ == '__main__':
    main()
