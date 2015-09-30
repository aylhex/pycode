# -*- coding: utf-8 -*-
from struct import pack
from binascii import crc32
import sys,re

def crc32unsigned(s, oldcrc = 0):
    value = crc32(s, oldcrc)
    if value < 0:
        value = 0xFFFFFFFF & value
    return value

def xorcode(s, key):
    klen = len(key)
    slen = len(s)
    value =  []
    for i in range(slen):
        value.append(pack('B', ord(s[i]) ^ ord(key[i%klen])))
    return "".join(value)

def str2bin(s):
    str_len = len(s)
    ret = []
    if str_len % 2 != 0:
        return ""
    try:
        for i in range(0, str_len, 2):
            val = int(s[i:i+2], 16)
            ret.append(chr(val))
    except Exception, e:
        return ""
    return "".join(ret)
    
def bin2str(bin_str):
    t = []
    for i in range(len(bin_str)):
        t.append("%02x"%(ord(bin_str[i]),))
    return "".join(t)

def print_bin(name,s):
    tmp = []
    for i in range(len(s)):
        tmp.append("%02x-"%(ord(s[i]),))
    print "%s len:%d,bin:%s\n"%(name, len(s), "".join(tmp),)

# little endian
def bin2int(s, size):
    ret = 0
    for i in range(size):
        ret += (ord(s[i]) << (i * 8))
    return ret

def i2a(ip):
    m = re.match('^(\d+)\.(\d+)\.(\d+)\.(\d+)$',ip)
    if not m:
        return 0
    return (int(m.group(1)) << 24) + (int(m.group(2)) <<16) + (int(m.group(3)) <<8) + int(m.group(4))

def a2i(arg):
    i = int(arg)
    return "%d.%d.%d.%d" % (i>>24, ((i&0x00FF0000) >> 16),((i&0x0000FF00) >> 8), (i&0x000000FF))

def main():
    # i = pack("=I", 1024);
    # print_bin("i", i)
    # print bin2int(i,4)
    import time
    t = time.time()
    for x in xrange(1,1000000):
        a2i(124562879)
    print time.time() - t
    t = time.time()

if __name__ == '__main__':
    main()
