#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 17:50:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，
对每月通话时间做个统计。
http://iservice.10010.com/e3/

https://uac.10010.com/portal/Service/CheckNeedVerify?callback=jQuery172013687745574861765_1430116978096&userNam
e=0756-2343242&pwdType=01&_=1430117020719
callback:jQuery172013687745574861765_1430116978096
userName:0756-2343242
pwdType:01
_:1430117020719

jQuery172013687745574861765_1430116978096({"resultCode":"false"});


https://uac.10010.com/portal/Service/MallLogin?callback=jQuery172013687745574861765_1430116978099&redirectURL=
http%3A%2F%2Fwww.10010.com&userName=18623451234&password=qwertyuiop&pwdType=01&productType=01&redirectType=03&rememberMe
=1&_=1430117306431

callback:jQuery172013687745574861765_1430116978099
redirectURL:http://www.10010.com
userName:18623451234
password:qwertyuiop
pwdType:01
productType:01
redirectType:03
rememberMe:1
_:1430117306431

callback:jQuery1720700501517392695_1430206366678
redirectURL:http://www.10010.com
userName:sfsd
password:sdfsasf
pwdType:01
productType:02
redirectType:03
rememberMe:1
areaCode:620
arrcity:珠海
_:1430206392652


jQuery172013687745574861765_1430116978099({resultCode:"7007",redirectURL:"http://www.10010.com",
    errDesc:"null",msg:'用户名或密码不正确。<a href="https://uac.10010.com/cust/resetpwd/inputName" target="
    _blank" style="color: #36c;cursor: pointer;text-decoration:underline;">忘记密码？</a>',needvode:"1",errorFrom:"cb"});


"""
import os
import requests
from bs4 import BeautifulSoup


def login(strurl):
    login_url=u'https://uac.10010.com/portal/Service/MallLogin'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.11 Safari/537.36',
        'Origin': 'http://bbs.vc52.cn',
        'Referer': 'http://bbs.vc52.cn/forum.php',
        'Host': 'bbs.vc52.cn',
    }
    # login_data={u'username':u'274047',u'password':u'cj200699812',u'quickforward':u'yes'}
    # params={'mod':'logging','action':'login','loginsubmit':'yes','infloat':'yes','lssubmit':'yes','inajax':1}
    params={
        u'callback':u'jQuery1720700501517392695_1430206366678',
        u'redirectURL':u'http://www.10010.com',
        u'userName':u'sfsd',
        u'password':u'sdfsasf',
        u'pwdType':u'01',
        u'productType':u'02',
        u'redirectType':u'03',
        u'rememberMe':u'1',
        u'areaCode':u'620',
        u'arrcity':u'珠海',
        u'_':u'1430206392652',
    }
    s = requests.Session()
    response=s.get(login_url,headers=headers,params=params)
    # print response.url
    print response.text.encode('utf-8')
    strhtml=s.get(strurl,cookies=response.cookies).text
    # print strhtml
    return strhtml

def getimglist(strhtml):
    htmlobj=BeautifulSoup(strhtml)
    imglist_tmp=htmlobj.find_all('img')
    imglist_tmp=filter(ifimgok, imglist_tmp)
    imglist=[imgobj.get('src') for imgobj in imglist_tmp]
    return imglist

def ifimgok(imgobj):
    imgclass=imgobj.get('class')
    if imgclass and u'zoom' in imgclass:
        return True
    else:
        return False

def main():
    strurl=u'http://bbs.vc52.cn/thread-658497-1-1.html'
    strhtml=login(strurl)
    imglist=getimglist(strhtml)
    print imglist

if __name__ == '__main__':
    main()
