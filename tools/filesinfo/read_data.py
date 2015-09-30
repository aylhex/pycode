#!/usr/bin/env python
# coding:utf-8

import os,sys
import hashlib
import win32api
import time,stat
import ctypes
import logging
import MySQLdb
dll = ctypes.windll.LoadLibrary(r'e:\code\python\res\getDigitalSigner.dll')
ISOTIMEFORMAT = '%Y-%m-%d %X'
LocalTime = time.strftime(ISOTIMEFORMAT, time.localtime())
extlist=['.exe','.dll','.sys','.khf']
def CreateMysqlConnect():
    try:
        sqlConnect = MySQLdb.connect(host='10.20.224.151', user='root', passwd='kingsoft', db='data')
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
    if filesuf not in ['.exe', '.dll']:
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
def updateLatestTime():
    curTime=str(time.time())
    con = CreateMysqlConnect()
    sqlCur = con.cursor()
    strsql = '''Update fileapp_file set detail = '%s' 
    where filename = 'all' 
    ''' % curTime
    result = sqlCur.execute(strsql)
    con.commit()
    return result
#------------------------------------------------
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
#---------------------------------------------
if __name__ == '__main__':
    #参数只需要1个，格式如：\\10.20.225.22\data_back\update_back_kmobile\201305\28\1445\
    if not len(sys.argv) == 2:  
        print 'parameters error'
        exit() 
    updatepath = sys.argv[1]
    if updatepath[-1] == '\\':
        updatepath = os.path.dirname(updatepath)
    if not os.path.isdir(updatepath):
        print '%s is Invalid.' % updatepath
        exit() 
    print 'updatepath is %s' % updatepath
    #creattime=getcreatetime(updatepath)
    channel = int(getchennelfrompath(updatepath))
    if not channel:
        print "Get data dir failed"
        exit() 
    print 'channel is %d' % channel
    dirpath = getupdatefiledirpath(updatepath)
    if not dirpath:
        print "Get old dir failed"
        exit() 
    print 'dirpath is %s' % dirpath
    updatefilepath = updatepath
    #filesinfo = getAllFilesInfo(dirpath, channel)
    #insertFileInfo(filesinfo, updatefilepath)
    #loger("Finish")

