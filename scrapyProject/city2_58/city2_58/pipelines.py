# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql


class City258Pipeline(object):

    def open_spider(self, spider):
    #     self.file = open('58_chuzu.txt', 'w', encoding='utf8')
    #     print('打开文件了')
    #
    # def process_item(self, item, spider):
    #     line = '{}\n'.format(json.dumps(dict(item), ensure_ascii=False))
    #     self.file.write(line)
    #     return item
        print('打开蜘蛛')

    def process_item(self, item, spider):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "test", charset="utf8")
        print('连接数据成功了')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 插入数据库
        cursor.execute("insert into test(name,price,url,introduce_item,address)values(%s,%s,%s,%s,%s)",
                       [item['name'], item['price'], item['url'], item['introduce_item'], item['address']])
        print('写入数据')
        # 提交
        db.commit()
        cursor.close()
        db.close()
        print('关闭数据库')
        print(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('关闭文件了')