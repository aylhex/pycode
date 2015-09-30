#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 13:26:36
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import sys
import os
import unittest
import logging
import time,stat
import read_data
#后续拼接数据路径用的字符串
strings='''
parms:
/? help
need 2 parms,
e.g.：
test.py kav2010 1508
test.py kxecom 1508
test.py kxeapp 1508

'''
#------------------------------
#常量定义
ISOTIMEFORMAT = '%Y-%m-%d %X'
#LocalTime = time.strftime(ISOTIMEFORMAT, time.localtime())
path_pre=r'\\10.20.223.55\data'
data_type_dict_pre={'kav2010':'update_back_kav2010',
                    'kxecom':'update_back_kxe_com',
                    'kxeapp':'update_back_kxe_app',}
data_root=r'\\10.20.220.119\dubarelease\updata'
data_type_dict={'kav2010':'UpdateIndex_kav2010',
                'kxecom':'UpdateIndex_kxe_com',
                'kxeapp':'UpdateIndex_kxe_app',}
kav_channel_list=['1508','1334','1509','1335','1337']
#data_res_root=data_root+os.sep+data_type_list[-1]+os.sep+'backFile'+os.sep+kav_channel_list[0]+os.sep
#----------------------
#日志模块
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler(os.path.join(os.getcwd(),'walk_auto.txt'),'w')
fh.setLevel(logging.DEBUG)
fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
fh.setFormatter(fm)
logger.addHandler(fh)
LOGA=logger.debug
#----------------------------------------------------------------------
def autoread():
    #获取最后更新时间
    latestime=read_data.GetLatestTime()
    LOGA('latestime: %s.%s.%s'%(latestime[0],latestime[1],latestime[2]))
    for data_type in data_type_dict.keys():
        for data_chl in kav_channel_list:
            LOGA('Start %s %s' %(data_type,data_chl))
            result=getdatapath(data_type,data_chl,latestime)
            if result:
                LOGA('%s %s finished!'%(data_type,data_chl))
    read_data.updateLatestTime()
#----------------------------------------------------------------------
def handtohand(path):
    """"""
    if os.path.exists(path) and path.find(path_pre)<>-1:
        path_res=path_223to119(path)
        if os.path.exists(path_res[0]):
            createtime=read_data.getcreatetime(path_res[0])
            get_file_info(path,createtime,path_res[1],path_res[2])
    else:
        print 'parm false'
def path_223to119(path):
    #\\10.20.223.55\data\update_back_kav2010\201308\28\1007
    path_res=[]
    try:
        if path[-1]=='\\':
            path==path[0:-1]
        slist=path.split('\\')
        temp_data_chl=read_data.getchennelfrompath(path)
        for temp_data_type in data_type_dict_pre.keys():
            if path.find(data_type_dict_pre[temp_data_type]):
                    #构造220.119上面的数据路径
                temp_path_res=os.path.join(data_root,data_type_dict[temp_data_type])
                temp_path_res=temp_path_res+os.sep+'backFile'+os.sep+str(temp_data_chl)+os.sep+slist[-3]+os.sep+slist[-2]+os.sep+slist[-1]
                path_res.append(temp_path_res)
                path_res.append(temp_data_type)
                path_res.append(temp_data_chl)
                return path_res
    except:
        return None
def path_119to223(path):
    #\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201308\28\1007
    path_dist=[]
    try:
        if path[-1]=='\\':
            path==path[0:-1]
        slist=path.split('\\')
        if slist[7] in kav_channel_list:
            temp_data_chl=slist[7]
            for item in data_type_dict.keys():
                if slist[5]==data_type_dict[item]:
                    temp_path_dist=os.path.join(path_pre,data_type_dict_pre[item])+os.sep+slist[-3]+os.sep+slist[-2]+os.sep+slist[-1]
                    path_dist.append(temp_path_dist)
                    path_dist.append(item)
                    path_dist.append(temp_data_chl)
                    return path_dist
    except:
        return None
    
def getdatapath(data_type,data_chl,latestime):
    if data_type_dict.has_key(data_type) and (data_chl in kav_channel_list):
        #构造220.119上面的数据路径
        path_res=os.path.join(data_root,data_type_dict[data_type])
        path_res=path_res+os.sep+'backFile'+os.sep+str(data_chl)+os.sep
        #构造223.55上对应的数据路径前缀
        path_dist=os.path.join(path_pre,data_type_dict_pre[data_type])+os.sep
        #得到220.119所有的数据源路径
        data_res_pathlist=data_everyday(path_res,latestime)
        count=len(data_res_pathlist)
        LOGA('coundt: %d' %count)
        #print 'coundt: %d' %count
        for item in data_res_pathlist:
            item_dist=item.replace(path_res,path_dist)
            #print item
            #print item_dist
            createtime=read_data.getcreatetime(item)
            get_file_info(item_dist,createtime,data_type,data_chl)
        #print 'all is OK !'
        return True
def data_everyday(path,latestime):
    #初始化列表，用来保存各个目录列表
    data_res_pathlist=[]
    month_list=[]
    day_list=[]
    time_list=[]
    #保存拼接出的每个目录绝对路径
    path_month=''
    path_day=''
    path_time=''
    #获取目录下月份的目录
    month_list=os.listdir(path)
    #排序
    month_list.sort()
    #遍历每个月份的目录
    for month in month_list:
        if int(month) < int(latestime[0]):
            continue
        path_month=os.path.join(path,month)
        day_list=os.listdir(path_month)
        day_list.sort()
        #遍历日期目录
        for day in day_list:
            if int(month) == int(latestime[0]) and int(day)<int(latestime[1]):
                continue
            path_day=os.path.join(path_month,day)
            time_list=os.listdir(path_day)
            time_list.sort()
            #遍历时间目录
            for times in time_list:
                if int(month) == int(latestime[0]) and int(day)==int(latestime[1]) and int(times) <int(latestime[2]):
                    continue
                path_time=os.path.join(path_day,times)
                path_dist=path_time.replace(path,path_pre)
                data_res_pathlist.append(path_time)
                #print path_time
                LOGA('data path:  %s' %path_time)
    return data_res_pathlist
#----------------------------------------------------------------------
def get_file_info(updatepath,createtime,data_type,data_chl):
    """"""
    #判断是否dir
    if not os.path.isdir(updatepath):
        #print '%s is Invalid.' % updatepath
        LOGA('%s is Invalid.' % updatepath)
        sys.exit() 
    if data_chl:
        data_chl=int(data_chl)
    #获取old目录
    oldpath = read_data.getupdatefiledirpath(updatepath)
    if not oldpath:
        #print "Get old dir failed"
        LOGA("Get old dir failed")
        exit() 
    #获取数据信息，保存在filesino中
    filesinfo = read_data.getAllFilesInfo(oldpath,data_type,data_chl)
    read_data.insertFileInfo(filesinfo, updatepath,createtime)
    #print updatepath+' update ok !'
    LOGA(updatepath+' update ok !')
if __name__=='__main__':
    if len(sys.argv)==1:
        autoread()
    else:
        path=sys.argv[1]
        #path=r'\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201308\28\1007'
        handtohand(path)

    
    
    
    