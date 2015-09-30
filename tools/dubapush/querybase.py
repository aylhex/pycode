# -*- coding: utf-8 -*-
import common
import urllib, urllib2

__channel__ = {0:"hCZHGrLSqVZLWvNN", 1:"nhQgpYWqeJDfWodG"}

class PostHeader(object):
    def __init__(self, ver=0, channelid=0):
        super(PostHeader, self).__init__()
        self.uid = common.str2bin('ffffffffffffffffffffffffffffffff')
        self.version = ver
        self.channelid = channelid
    def pack(self):
        return "%s%s" % (common.pack("=H", self.version), self.uid)

#post data need drived from PostBodyBase
class PostBodyBase(object):
    """docstring for PostBodyBase"""
    def __init__(self):
        super(PostBodyBase, self).__init__()
    def pack(self):
        raise Exception("you need overwrite pack() mathod!")

class HttpUrl(object):
    """docstring for HttpUrl"""
    def __init__(self, site, port=80, path='/'):
        super(HttpUrl, self).__init__()
        self.url = 'http://%s:%s%s' % (site, port, path)
        print self.url
        
class Request(object):
    """docstring for Request"""
    def __init__(self, header, body):
        super(Request, self).__init__()
        self.header = header
        post_data = "%s%s" % (self.header.pack(), body.pack())
        post_data = common.pack("=H", self.header.channelid) + common.xorcode(post_data, __channel__[self.header.channelid])
        crc = common.crc32unsigned(post_data)
        crc = common.crc32unsigned(__channel__[self.header.channelid], crc)
        self.req_data = "%s%s" % (common.pack("=HI", len(post_data)+6, crc), post_data)

    def request(self, httpUrl):
        req = urllib2.Request(httpUrl.url)
        f = urllib2.urlopen(req, self.req_data)
        self.response = ''
        if f:
            self.response = f.read()
            f.close()
        return self.response

    def decode(self):
        ret = common.xorcode(self.response[6:], __channel__[self.header.channelid]).decode("utf-8")     
        # print ret
        return ret

def __weatherTest__():
    class WeatherBody(PostBodyBase):
        """docstring for WeatherBody"""
        def __init__(self, userSetCityid, lastLocateCityid, infotype):
            super(WeatherBody, self).__init__()
            self.body = common.pack("=IIH", userSetCityid, lastLocateCityid, infotype)
        def pack(self):
            return self.body
    url = HttpUrl('wq.cloud.duba.net', path='/weather_query2')
    head = PostHeader()
    body = WeatherBody(101010100, 0, 0xff)
    req = Request(head, body)
    req.request(url)
    req.decode()
            
def __main__():
    __weatherTest__()

if __name__ == '__main__':
    __main__()
