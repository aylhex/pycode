#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/8/7

import sys
import socket
import time
struct='%Y-%m-%d %X'
#----------------------------------------------------------------------
def main():
    """"""
    host=''
    port=55361
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()
    print 'Socket Created'
    try:
        s.bind((host,port))
    except socket.error,msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    print 'Socket bind complete'
    s.listen(10)
    print 'Socket now listening'
    while True:
        conn,addr=s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        #conn.settimeout(5)
        while True:
            try:
                data=conn.recv(1024)
                reply='accept:'+data
                print '%s (%s): %s' %(time.strftime(struct,time.localtime()),addr[0],data)
                conn.send(reply)
            except socket.error,msg:
                print 'error code : '+str(msg[0])
                break
        conn.close()
    s.close()
if __name__=='__main__':
    main()