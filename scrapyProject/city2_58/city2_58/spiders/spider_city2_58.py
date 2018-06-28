# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City258Item
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

# class SpiderCity258Spider(scrapy.Spider):
# 改为分布式存储
class SpiderCity258Spider(RedisSpider):
    name = 'spider_city2_58'
    allowed_domains = ['58.com']
    start_urls = ['http://sz.58.com/chuzu/']

    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li').items()
        print('li_list:', type(li_list))
        print('li_list', li_list)
        for it in li_list:
            a_tag = it('div.des > h2 > a')
            item = City258Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.listliright > div.money > b').text()

            yield item
        if not li_list:
            return
        pn = response.meta.get('pn', 1)
        pn += 1
        response.meta['pn'] = pn
        if pn > 5:
            return
        req = response.follow('/chuzu/pn{}/'.format(pn),
                              callback=self.parse,
                              meta={'pn':pn})
        yield req

    def error_back(self, e):
        _ = self
        print(e)
        print('报错了！')

        #  redis测试
        #     if item['url']:
        #         yield Request(item['url'],
        #                       callback=self.detail_parse,
        #                       meta={'item':item}, #使用meta参数，把item传给detail_parse()
        #                       priority=10,
        #                       dont_filter=True
        #                       )
        #
        # url = jpy('#bottom_ad_li > div.pager > a.next').attr('href') #提取翻页链接
        # test_request = Request(url,
        #                        callback=self.parse,
        #                        priority=10,
        #                        # meta={'dont_redirect': True}
        #                        dont_filter=True  # 对url不过滤
        #                        )
        # print('翻页')
        # yield test_request #实现翻页

    # def detail_parse(self, response):
    #     jpy = PyQuery(response.text)
    #     item = response.meta['item'] #接收item
    #     item['introduce_item'] = jpy('body > div.main-wrap > div.house-detail-desc > div.main-detail-info.fl > div.house-word-introduce.f16.c_555 > ul > li:nth-child(1) > span.a2').text()  # 提取房屋亮点
    #     item['address'] = jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc > div.house-desc-item.fl.c_333 > ul > li:nth-child(6) > span.dz').text()  #房屋详情地址
    #     item['phone_number'] = jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-fraud-tip > div.house-chat-phone > span').text()
    #     return item