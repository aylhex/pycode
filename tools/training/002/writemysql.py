#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import MySQLdb


def createmysqlcon():
    try:
        con = MySQLdb.connect(
            host='10.20.225.96', user='root', passwd='kingsoft', db='test')
        return con
    except:
        return None


def getcodefromtxt(txtpath):
    try:
        fp = open(txtpath, 'r')
        for line in fp.readlines():
            yield line
    except IOError:
        return None


def insertdb(con, codelist):
    sqlCur = con.cursor()
    for i in codelist:
        strsql = """insert into activecode  values ('%s');""" % i.replace(
            '\n', '')
        sqlCur.execute(strsql)
    con.commit()


def main():
    con = createmysqlcon()
    codelist = getcodefromtxt('activecode.txt')
    result = insertdb(con, codelist)
    con.close()

if __name__ == '__main__':
    main()
