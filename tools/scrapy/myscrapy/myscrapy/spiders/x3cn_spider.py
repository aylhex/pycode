#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-05-02 15:45:43
# @Author  : chen jun (chenjun2@kingsoft.com)
# @Link    : www.ijinshan.com
# @Version : $Id$

import os
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from myscrapy.items import x3cn_Item

class X3cnSpider(BaseSpider):
    """docstring for X3cnSpider
    http://www.x3cn.com/thread-433036-1-1.html

    """
    name="x3cn"
    allowed_domains=["www.x3cn.com"]
    start_urls=[
        "http://www.x3cn.com/thread-433036-1-1.html",
    ]
    def parse(self,response):
        # filename=os.path.basename(response.url).split(r'.')[0]
        # open(filename,'wb').write(response.bady)
        items=[]
        hxs=HtmlXPathSelector(response)
        sites=hxs.path("//td[@id='postmessage_6511893']/a")
        for site in sites:
            item=x3cn_Item()
            item['title']=site.path("text()").extract()
            item['link']=site.path("@href").extract()
            items.append(item)
        return items