#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import arrow
import datetime

"""
格式化对应字符:

Year            YYYY    2000, 2001, 2002 ... 2012, 2013
                YY      00, 01, 02 ... 12, 13
Month           MMMM    January, February, March ...
                MMM     Jan, Feb, Mar ...
                MM      01, 02, 03 ... 11, 12
                M       1, 2, 3 ... 11, 12
Day of Year     DDDD    001, 002, 003 ... 364, 365
                DDD     1, 2, 3 ... 4, 5
Day of Month    DD      01, 02, 03 ... 30, 31
                D       1, 2, 3 ... 30, 31
Day of Week     dddd    Monday, Tuesday, Wednesday ...
                ddd     Mon, Tue, Wed ...
                d       1, 2, 3 ... 6, 7
Hour            HH      00, 01, 02 ... 23, 24
                H       0, 1, 2 ... 23, 24
                hh      01, 02, 03 ... 11, 12
                h       1, 2, 3 ... 11, 12
AM / PM         A       AM, PM
                a       am, pm
Minute          mm      00, 01, 02 ... 58, 59
                m       0, 1, 2 ... 58, 59
Second          ss      00, 01, 02 ... 58, 59
                s       0, 1, 2 ... 58, 59
Sub-second      SSS     000, 001, 002 ... 998, 999
                SS      00, 01, 02 ... 98, 99
                S       0, 1, 2 ... 8, 9
Timezone        ZZ      -07:00, -06:00 ... +06:00, +07:00
                Z       -0700, -0600 ... +0600, +0700
Timestamp       X       1381685817

Parameters:
year – the calendar year.
month – the calendar month.
day – the calendar day.
hour – (optional) the hour. Defaults to 0.
minute – (optional) the minute, Defaults to 0.
second – (optional) the second, Defaults to 0.
microsecond – (optional) the microsecond. Defaults 0.
tzinfo – (optional) the tzinfo object. Defaults to None.

更改当前时间对象，支持替换或者在已有数值基础上计算
replace(**kwargs)
arw.replace(year=2014, month=6)
arw.replace(years=1, months=-1)
针对某个单位，生成二元元祖，从该单位起始到结束


""" 


truct="YYYY-MM-DD HH:mm:ss"
    

def getmytime():
    # 获取时间对象
    ctime = arrow.now()
    # ctime = arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
    # ctime = arrow.get('2013-09-30T15:34:00.000-07:00')
    # ctime = arrow.get("2015-10-28")
    # ctime = arrow.get(2013, 5, 5)
    # ctime = arrow.Arrow(2013, 5, 5)
    # ctime = arrow.get('23333')
    # ctime = arrow.get(1367900664.152325)
    # ctime = arrow.get(datetime.utcnow())
    # ctime = arrow.get(datetime.now(), 'US/Pacific')

    # ctime方法
    # ctime = ctime.to('US/Pacific')
    # ctime = ctime.to('local')   
    # ctime = ctime.to('utc')
    ctime2 = ctime.replace(hour=2, minute=10,weeks=-1)

    # 属性访问
    print ctime.format(truct)
    print ctime.timestamp
    print ctime.datetime
    print ctime.naive
    print ctime.tzinfo
    print ctime.year
    print ctime.month
    print ctime.day
    print ctime.hour
    print ctime.minute
    print ctime.second
    print ctime.date()
    print ctime.time()
    print ctime.weekday()
    print ctime.humanize()

    print ctime2.format(truct)
    print ctime2.humanize(ctime)

def Getarrow():
    starttime = arrow.get("2015-10-28")
    stoptime = starttime.replace(weeks=1,minute=25)
    # get the list or time
    # the parmas can be year month day hour 
    for dt in arrow.Arrow.range("hour",starttime,stoptime):
        print dt.format(truct)
    for dt in arrow.Arrow.span_range("hour",starttime,stoptime):
        print dt.format(truct)

def GetSpan():
    ctime = arrow.utcnow()
    print ctime.span('hour')
    print ctime.floor('hour')
    print ctime.ceil('hour')

def GetSubTime():
    ctime1 = arrow.now().timestamp
    ctime2 = arrow.get(1344533444).timestamp
    sss = ctime1-ctime2
    print sss

def main():
    # getmytime()
    # Getarrow()
    GetSubTime()

if __name__ == '__main__':
    main()