#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2013/8/7

import sys
import socket
remote_ip='10.20.224.191'
port=1099
message = "GET / HTTP/1.1"
def main():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()
    print 'Socket Created'
    print 'remote_ip:'+ remote_ip
    s.connect((remote_ip,port))
    print 'Socket Connected to  '+remote_ip
    s.send(message)
    print s.recv(4096)
    while True:
        try:
            msg=raw_input('Send>>>')
            if msg=='quit':
                sys.exit()
            s.send(msg)
        except socket.error:
            print 'Send failed!!'
            sys.exit()
        reply = s.recv(4096)
        print reply
    s.close()
if __name__=='__main__':
    main()