#!/usr/bin/env python
# coding:utf-8

import os,sys
import hashlib
import win32api
import time,stat
import ctypes
import logging
import MySQLdb
from xml.etree import ElementTree
#初始化变量
dll = ctypes.windll.LoadLibrary(r'e:\kuaipan\study\code\python\mycode\getDigitalSigner.dll')
ISOTIMEFORMAT = '%Y-%m-%d %X'
LocalTime = time.strftime(ISOTIMEFORMAT, time.localtime())
extlist=['.exe','.dll','.sys','.khf']
path_pre=r'\\10.20.223.55\data'
data_type_dict_pre={'kav2010':'update_back_kav2010',
                    'kxecom':'update_back_kxe_com',
                    'kxeapp':'update_back_kxe_app',}
data_root=r'\\10.20.220.119\dubarelease\updata'
data_type_dict={'kav2010':'UpdateIndex_kav2010',
                'kxecom':'UpdateIndex_kxe_com',
                'kxeapp':'UpdateIndex_kxe_app',}
kav_channel_list=['1508','1334','1509','1335','1337']
data2time='197001-01-1200'
#日志模块
def logger():
    """"""
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh=logging.FileHandler(os.path.join(os.getcwd(),'log.txt'),'a')
    fh.setLevel(logging.DEBUG)
    fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fm)
    logger.addHandler(fh)
    debug=logger.debug
    return debug
#-----------------
def CreateMysqlConnect():
    try:
        sqlConnect = MySQLdb.connect(host='127.0.0.1', user='user', passwd='pwd', db='data')
        return sqlConnect
    except (Exception):
        print 'sql connect to localhost failed'
    return None
#---------------------------------------------
def getFileMd5(filepath):
    tempfile = None
    bRet = False
    strMd5 = ""
    try:
        tempfile = open(filepath, "rb")
        md5 = hashlib.md5()
        strRead = ""
        
        while True:
            strRead = tempfile.read(8096)
            if not strRead:
                break
            md5.update(strRead)
        #read file finish
        bRet = True
        strMd5 = md5.hexdigest()
    except:
        bRet 
    finally:
        if tempfile:
            tempfile.close()

    #return [bRet, strMd5]
    return strMd5
#---------------------------------------------
def getFileVersion(filepath):
    filesuf = os.path.splitext(filepath)[1]
    if filesuf not in extlist:
        return ''
    try:
        info = win32api.GetFileVersionInfo(filepath, os.sep)  
        ms = info['FileVersionMS']  
        ls = info['FileVersionLS']  
        version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
        return version
    except:
        print "get %s version error" % filepath
        return ''
#---------------------------------------------
def getFileSize(filepath):
    #filesizetemp=int(os.path.getsize(filepath))
    #if filesizetemp>=0 and filesizetemp<=999:
        #filesize=str(filesizetemp)+' B'
    #elif filesizetemp>=1000 and filesizetemp<=999999:
        #filesize=str(filesizetemp/1024)+' KB'
    #elif filesizetemp>=1000000 and filesizetemp<=999999999:
        #filesize=str(filesizetemp/1048576)+' MB'
    #elif filesizetemp>=1000000000 and filesizetemp<=999999999999:
        #filesize=str(filesizetemp/1073741824)+' GB'
    #else:
        #filesize=str(filesizetemp)+' B'
    #return filesize
    try :
        return os.path.getsize(filepath)
    except:
        return ''
#---------------------------------------------
def getRelativePath(root, filepath):
    filename = os.path.basename(filepath)
    RelativePath = filepath.rsplit(filename, 1)[0].replace(root, '', 1)
    return RelativePath
#---------------------------------------------

#def getLocalTime():
    #ISOTIMEFORMAT = '%Y-%m-%d %X'
    #return  time.strftime(ISOTIMEFORMAT, time.localtime())

def getDigitalSigner(filepath):
    if os.path.splitext(filepath)[1] not in extlist:
        return None
    pStr = ctypes.c_wchar_p(filepath)
    temp = dll.GetDigitalSigner(pStr)
    result = ctypes.c_wchar_p(temp).value
    if result:
        return result
    return None
#---------------------------------------------
def getFileInfo(root, filepath, data_type,channel):
    filename = os.path.basename(filepath)
    filesize = getFileSize(filepath)
    filemd5 = getFileMd5(filepath)
    filerelativepath = getRelativePath(root, filepath)
    fileversion = getFileVersion(filepath)
    filesigner = getDigitalSigner(filepath)
    return {'filename' : filename, 
            'fileversion' : fileversion, 
            'filesize' : filesize, 
            'filemd5' : filemd5, 
            'localfilepath' : filerelativepath.replace('\\', '\\\\'), 
            'type':data_type,
            'channel' : channel,
            'digital_signature' : filesigner,
            }
#---------------------------------------------
def checkNeedFile(filename):
    filesuf = os.path.splitext(filename)[1]
    if filesuf in extlist:
        return True
    else:
        return False
#---------------------------------------------
def getAllFiles(dirpath):
    allfiles = []
    for root, dirs, files in os.walk(dirpath):
        #if os.path.join(dirpath, 'ktool_update') in root:
            #continue
        #if os.path.join(dirpath, 'appdata') in root:
            #continue
        #if os.path.join(dirpath, 'download') in root:
            #continue
        for item in files:
            #if checkNeedFile(item):
            allfiles.append(os.path.join(root, item))
    return allfiles
#---------------------------------------------
def getAllFilesInfo(dirpath, data_type,channel):
    needfiles = getAllFiles(dirpath)
    return [getFileInfo(dirpath, filepath, data_type,channel) for filepath in needfiles]
#---------------------------------------------
def getInsertSQL(eachfileinfo, updatefilepath,createtime):
    strsql = ''
    if eachfileinfo['digital_signature']:
        strsql = '''Insert Into fileapp_file (filename, channel,chnltype, fileversion, filesize, filemd5, localfilepath, publishtime, updatefilepath, digital_signature) 
     values ('%s', '%d','%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s')
     ''' % (eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['type'], eachfileinfo['fileversion'], eachfileinfo['filesize'], 
            eachfileinfo['filemd5'], eachfileinfo['localfilepath'], createtime, updatefilepath.replace('\\', '\\\\'), eachfileinfo['digital_signature'])
    else:
        strsql = '''Insert Into fileapp_file (filename, channel, chnltype,fileversion, filesize, filemd5, localfilepath, publishtime, updatefilepath) 
     values ('%s', '%d','%s', '%s', '%d', '%s', '%s', '%s', '%s')
     ''' % (eachfileinfo['filename'], eachfileinfo['channel'],  eachfileinfo['type'], eachfileinfo['fileversion'],
            eachfileinfo['filesize'], eachfileinfo['filemd5'], eachfileinfo['localfilepath'], createtime, updatefilepath.replace('\\', '\\\\'))
    return strsql
#---------------------------------------------
def getQuerySQL(eachfileinfo,updatefilepath):
    strsql = '''Select filename from fileapp_file 
    where filename = '%s' and channel = '%d' and updatefilepath = '%s'    
    ''' % (eachfileinfo['filename'], eachfileinfo['channel'], updatefilepath.replace('\\', '\\\\'))
    return strsql
#---------------------------------------------
def getUpdateSQL(eachfileinfo,createtime):
    strsql = '''Update fileapp_file set lapsetime = '%s' 
    where filename = '%s' and channel = '%d' and localfilepath = '%s' and lapsetime IS null
    ''' % (createtime, eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['localfilepath'])
    return strsql
#---------------------------------------------
#从数据库获取最后一次更新的时间并转化
#返回 列表  ['201309', '25', '2213']
def GetLatestTime():
    con = CreateMysqlConnect()
    sqlCur = con.cursor()
    strsql='''Select detail from fileapp_file 
    where filename = 'all' 
    '''
    sqlCur.execute(strsql)
    ltime=int(sqlCur.fetchone()[0])
    #return ltime
    truct='%Y%m %d %H%M'
    ltime=time.localtime(ltime)
    ltime=time.strftime(truct,ltime)
    ltime=ltime.split()
    return ltime
#更新数据库时间
#传入的时间必须为如下格式'201310-25-1220'
def updateLatestTime():
    curTime=str(int(time.time())-108000)
    con = CreateMysqlConnect()
    sqlCur = con.cursor()
    strsql = '''Update fileapp_file set detail = '%s' 
    where filename = 'all' 
    ''' % curTime
    result = sqlCur.execute(strsql)
    con.commit()
    return result
#------------------------------------------------
#检查数据库中文件信息是否存在
def fileinfoExists(sqlCur, eachfileinfo,updatefilepath):
    querysql = getQuerySQL(eachfileinfo,updatefilepath)
    sqlCur.execute(querysql)
    data = sqlCur.fetchall()
    if len(data) > 0:
        return True
    else:
        return False
#---------------------------------------------    
def updateFileinfo(con, sqlCur, eachfileinfo,createtime):
    querysql = getUpdateSQL(eachfileinfo,createtime)
    result = sqlCur.execute(querysql)
    con.commit()
    return result
#---------------------------------------------
def insertFileInfo(FilesInfo, updatefilepath,createtime):
    con = CreateMysqlConnect()
    sqlCur = con.cursor()
    #createtime=getcreatetime(updatefilepath)
    for eachfileinfo in FilesInfo:
        if fileinfoExists(sqlCur, eachfileinfo,updatefilepath):
            print "This %s has existed in db." % eachfileinfo['filename']
            continue
        updateFileinfo(con, sqlCur, eachfileinfo,createtime)
        querysql = getInsertSQL(eachfileinfo, updatefilepath,createtime)
        sqlCur.execute(querysql)
        con.commit()
        print "%s\t has insert into DB successfully." % eachfileinfo['filename']
#---------------------------------------------
#获取kav2010频道的数据tryno，不推荐使用，较局限
def getchennelfrompath(updatepath):
    temppath = r'\anon_root\duba\2010\bin'
    path = updatepath + temppath
    if not os.path.isdir(path):
        return False
    if os.listdir(path):
        return os.listdir(path)[0]
    else:
        return False
#---------------------------------------------
#拼接old目录
def getupdatefiledirpath(updatepath):
    temppath = r'\old'
    path = updatepath + temppath
    if not os.path.isdir(path):
        return False
    return path
#---------------------------------------------
def loger():    
    #日志模块
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh=logging.FileHandler(os.path.join(os.getcwd(),'log.txt'),'w')
    fh.setLevel(logging.DEBUG)
    fm=logging.Formatter("%(asctime)s  %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fm)
    logger.addHandler(fh)
    Loger=logger.debug
    return Loger
#----------------------------------------------------------------------
def getcreatetime(updatepath):
    """"""
    st=os.stat(updatepath)
    create_time=st[stat.ST_CTIME]
    #size=st[stat.ST_SIZE]
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    LocalTime = time.strftime(ISOTIMEFORMAT, time.localtime(create_time))
    return LocalTime
def path_223to119(path):
    #\\10.20.223.55\data\update_back_kav2010\201308\28\1007
    path_res=[]
    try:
        if path[-1]=='\\':
            path==path[0:-1]
        slist=path.split('\\')
        temp_data_chl=getchennelfrompath(path)
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
        return ['','','',]
    
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
            createtime=read_data.getcreatetime(item)
            #get_file_info(item_dist,createtime,data_type,data_chl)
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
                getdata_date(path_time)
                data_res_pathlist.append(path_time)
                #print path_time
                LOGA('data path:  %s' %path_time)
    return data_res_pathlist
#---------------------------------------------
def getdata_date(datapath):
    datapath_list=datapath.split('\\')
    data_time=datapath_list[-3]+datapath_list[-2]+datapath_list[-1]
    if int(data_time)>int(data2time):
        data2time=data_time
def xml_parse(xmlfile):
    f=open(xmlfile).read()
    # Get the infomations from the recv_xml.  
    xml_recv = ElementTree.fromstring(f)  
    node_files=xml_recv.getiterator('file')[0].getchildren()
    node_dirs=xml_recv.getiterator('dir')[0].getchildren()
    node_files=[item.attrib.get('path','').strip() for item in node_files]
    node_dirs=[item.attrib.get('path','').strip() for item in node_dirs]
    return (node_dirs,node_files)
        
if __name__ == '__main__':
    print 'start'

