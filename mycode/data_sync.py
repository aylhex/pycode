#!/usr/bin/env python
#coding:utf-8
# Author:   --<cj>
# Purpose: 
# Created: 2013/10/28

import sys
import os
import read_data
#----------------------------------------------------------------------
def autoget(time):
    """time :
    201309-12-1222
    """
    ltime=time.split('-')
def autoread(time):
    #latestime=read_data.GetLatestTime()
    #LOGA('latestime: %s.%s.%s'%(latestime[0],latestime[1],latestime[2]))
    for data_type in data_type_dict.keys():
        for data_chl in kav_channel_list:
            #LOGA('Start %s %s' %(data_type,data_chl))
            result=read_data.getdatapath(data_type,data_chl,time)
            #if result:
                #LOGA('%s %s finished!'%(data_type,data_chl))

if __name__=='__main__':
    time='201310-25-1000'
    