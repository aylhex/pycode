#!/usr/bin/env python
# coding:utf-8

import MySQLdb
import os
import hashlib
import win32api
import time
import sys
import ctypes

dll = ctypes.windll.LoadLibrary(r'c:\Python27\getDigitalSigner.dll')

ISOTIMEFORMAT = '%Y-%m-%d %X'
LocalTime = time.strftime(ISOTIMEFORMAT, time.localtime())

def CreateMysqlConnect():
    try:
        sqlConnect = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='test')
        return sqlConnect
    except (Exception):
        print 'sql connect to localhost failed'
    return None

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

def getFileSize(filepath):
    return os.path.getsize(filepath)

def getRelativePath(root, filepath):
    filename = os.path.basename(filepath)
    RelativePath = filepath.rsplit(filename, 1)[0].replace(root, '', 1)
    return RelativePath
    

def getLocalTime():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return  time.strftime(ISOTIMEFORMAT, time.localtime())

def getDigitalSigner(filepath):
    if os.path.splitext(filepath)[1] not in ['.exe', '.dll', '.sys']:
        return None
    pStr = ctypes.c_wchar_p(filepath)
    temp = dll.GetDigitalSigner(pStr)
    result = ctypes.c_wchar_p(temp).value
    if result:
        return result
    return None

def getFileInfo(root, filepath, channel):
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
            'channel' : channel,
            'digital_signature' : filesigner,
            }

def checkNeedFile(filename):
    suffixlist = ['.exe', '.dll', '.dat', '.apk']
    filesuf = os.path.splitext(filename)[1]
    if filesuf in suffixlist:
        return True
    else:
        return False

def getAllFiles(dirpath):
    allfiles = []
    for root, dirs, files in os.walk(dirpath):
        if os.path.join(dirpath, 'ktool_update') in root:
            continue
        if os.path.join(dirpath, 'appdata') in root:
            continue
        if os.path.join(dirpath, 'download') in root:
            continue
        for item in files:
            if checkNeedFile(item):
                allfiles.append(os.path.join(root, item))
    return allfiles

def getAllFilesInfo(dirpath, channel):
    needfiles = getAllFiles(dirpath)
    return [getFileInfo(dirpath, filepath, channel) for filepath in needfiles]

def getInsertSQL(eachfileinfo, updatefilepath):
    strsql = ''
    if eachfileinfo['digital_signature']:
        strsql = '''Insert Into fileapp_file (filename, channel, fileversion, filesize, filemd5, localfilepath, publishtime, updatefilepath, digital_signature) 
     values ('%s', '%d', '%s', '%d', '%s', '%s', '%s', '%s', '%s')
     ''' % (eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['fileversion'], eachfileinfo['filesize'], 
            eachfileinfo['filemd5'], eachfileinfo['localfilepath'], LocalTime, updatefilepath.replace('\\', '\\\\'), eachfileinfo['digital_signature'])
    else:
        strsql = '''Insert Into fileapp_file (filename, channel, fileversion, filesize, filemd5, localfilepath, publishtime, updatefilepath) 
     values ('%s', '%d', '%s', '%d', '%s', '%s', '%s', '%s')
     ''' % (eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['fileversion'],
            eachfileinfo['filesize'], eachfileinfo['filemd5'], eachfileinfo['localfilepath'], LocalTime, updatefilepath.replace('\\', '\\\\'))
    return strsql

def getQuerySQL(eachfileinfo):
    strsql = '''Select filename from fileapp_file 
    where filename = '%s' and channel = '%d' and filemd5 = '%s'    
    ''' % (eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['filemd5'])
    return strsql

def getUpdateSQL(eachfileinfo):
    strsql = '''Update fileapp_file set lapsetime = '%s' 
    where filename = '%s' and channel = '%d' and localfilepath = '%s' and lapsetime IS null
    ''' % (LocalTime, eachfileinfo['filename'], eachfileinfo['channel'], eachfileinfo['localfilepath'])
    return strsql

def fileinfoExists(sqlCur, eachfileinfo):
    querysql = getQuerySQL(eachfileinfo)
    sqlCur.execute(querysql)
    data = sqlCur.fetchall()
    if len(data) > 0:
        return True
    else:
        return False
    
def updateFileinfo(con, sqlCur, eachfileinfo):
    querysql = getUpdateSQL(eachfileinfo)
    result = sqlCur.execute(querysql)
    con.commit()
    return result

def insertFileInfo(FilesInfo, updatefilepath=''):
    con = CreateMysqlConnect()
    sqlCur = con.cursor()
    for eachfileinfo in FilesInfo:
        if fileinfoExists(sqlCur, eachfileinfo):
            print "This %s has existed in db." % eachfileinfo['filename']
            continue
        updateFileinfo(con, sqlCur, eachfileinfo)
        querysql = getInsertSQL(eachfileinfo, updatefilepath)
        print querysql
        sqlCur.execute(querysql)
        con.commit()

def main():
    dirpath = r'c:\Program Files (x86)\Shoujizhushou'     
    channel = 2001
    filesinfo = getAllFilesInfo(dirpath, channel)
    insertFileInfo(filesinfo)

def getchennelfrompath(updatepath):
    temppath = r'\anon_root\kmobile\bin'
    path = updatepath + temppath
    if not os.path.isdir(path):
        return False
    if os.listdir(path):
        return os.listdir(path)[0]
    else:
        return False

def getupdatefiledirpath(updatepath):
    temppath = r'\old'
    path = updatepath + temppath
    if not os.path.isdir(path):
        return False
    return path

if __name__ == '__main__':
    if not len(sys.argv) == 2:  #参数只需要1个，格式如：\\10.20.225.22\data_back\update_back_kmobile\201305\28\1445\
        print 'parameters error'
        exit() 
    updatepath = sys.argv[1]
    if updatepath[-1] == '\\':
        updatepath = os.path.dirname(updatepath)
        
    if not os.path.isdir(updatepath):
        print '%s is Invalid.' % updatepath
        exit() 
    print 'updatepath is %s' % updatepath
    
    channel = int(getchennelfrompath(updatepath))
    if not channel:
        print "Get kmobile dir failed"
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

