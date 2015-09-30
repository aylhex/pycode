# -*- coding: utf-8 -*-
from querybase import *

class Location(object):
    """docstring for Location"""
    def __init__(self, province, city, town):
        super(Location, self).__init__()
        self.country = 101
        self.province = province
        self.city = city
        self.town = town
    def pack(self):
        return common.pack("4B", self.country, self.province, self.city, self.town)

class VerInfo(object):
    """docstring for VerInfo"""
    def __init__(self, dubaver, dubarbver, cliver, osver):
        super(VerInfo, self).__init__()
        self.dubaver = dubaver
        self.dubarbver = dubarbver
        self.cliver = cliver
        self.osver = osver
        print "client version:", self.cliver
    def pack(self):
        return common.pack("=4I", self.dubaver, self.dubarbver, self.cliver, self.osver)

class HardwareInfo(object):
    """docstring for HardwareInfo"""
    def __init__(self, cpu, disk, ram):
        super(HardwareInfo, self).__init__()
        self.cpu = cpu
        self.disk = disk
        self.ram = ram
    def pack(self):
        return common.pack("=3H", self.cpu, self.disk, self.ram)

#return int32 of setted bits, bits 0~31
def setBits(*bits):
    target = 0
    for bit in bits:
        target |= (0x01 << bit)
    return target

class PubInfo(object):
    """docstring for PubInfo"""
    def __init__(self, tryno, pushtype, scene=0, games=[0,0,0,0], websites=[0,0,0,0], coexist=0, viplevel=0, userattr=0):
        super(PubInfo, self).__init__()
        self.tryno = tryno
        self.pushtype = pushtype
        self.scene = scene
        self.games = games
        self.websites = websites
        self.coexist = coexist
        self.viplevel = viplevel
        self.userattr = userattr
        print "tyrno=%s, push_type=%s" % (tryno, pushtype)
    def pack(self):
        return common.pack("=H2B4H4HIBH", self.tryno, self.pushtype, self.scene, self.games[0], self.games[1], self.games[2], self.games[3], \
            self.websites[0], self.websites[1], self.websites[2], self.websites[3], self.coexist, self.viplevel, self.userattr)
class V1Patch(object):
    """docstring for V1Patch"""
    def __init__(self, ruleid):
        super(V1Patch, self).__init__()
        self.ruleid = ruleid
    def pack(self):
        return common.pack('=I', self.ruleid)

class V1Patch(object):
    """docstring for V1Patch"""
    def __init__(self, ruleid):
        super(V1Patch, self).__init__()
        self.ruleid = ruleid
    def pack(self):
        return common.pack('=I', self.ruleid)

def contentTest():
    class ContentBody(PostBodyBase):
        """docstring for ContentBody"""
        def __init__(self, loc, ver, hardware, pub, v1patch=None):
            super(ContentBody, self).__init__()
            self.body = '%s%s%s%s' % (loc.pack(), ver.pack(), hardware.pack(), pub.pack())
            if v1patch:
                self.body += v1patch.pack()
        def pack(self):
            return self.body

    header = PostHeader(ver=1)

    loc = Location(24, 1, 1)
    ver = VerInfo(1344080121, 1344080121, 14, 201403)
    hardware = HardwareInfo(2000, 3, 5)
    pub = PubInfo(1335, 2, 0, coexist=setBits(0), viplevel=1, userattr=setBits(2), games=[123,0,0,0], websites=[123,0,0,0])
    contentbody = ContentBody(loc, ver, hardware, pub, v1patch=V1Patch(0))

    # url = HttpUrl("10.20.216.114", path='/content_push')
    # url = HttpUrl('wq.cloud.duba.net', path='/content_push')
    url = HttpUrl("10.20.216.123", path='/content_push')

    req = Request(header, contentbody)
    req.request(url)
    ret = req.decode()
    ret = ret[:ret.rfind('}')+1]
    import json,base64
    ret = json.loads(ret)
    if "content" in ret:
        print "ruleid:", ret["ruleid"]
        print base64.b64decode(ret['content'])
    else:
        print ret


def main():
    contentTest()

if __name__ == '__main__':
    main()
