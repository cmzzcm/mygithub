#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
from pyquery import PyQuery
import MySQLdb as mdb
import traceback

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# wait = WebDriverWait(driver, 10)

elem =driver.find_element_by_xpath('//*[@id="kw"]')
elem.send_keys("手机商城", Keys.ENTER)
# wait = WebDriverWait(driver, 3000)
driver.implicitly_wait(30) # 隐性等待，最长等30秒
# print(driver.page_source)
# html = driver.page_source
# '//*[@id="5"]/div/div[2]/div[2]/a[1]'
#\35 > div > div.c-span18.c-span-last > div.f13 > a.c-showurl
# //*[@id="3"]/div/div[2]/div[2]/a[1]
# pattern = re.compile('.*?华为商城官网.*?http://(.*?)}">', re.S)
# re.findall(pattern, html)
# //*[@id="5"]/div/div[2]/div[2]/a[1]
url2 = driver.find_element_by_xpath('//*[@id="5"]/div/div[2]/div[2]/a[1]').text
# url2 = driver.find_element_by_xpath('//*[@id="3"]/div/div[2]/div[2]/a[1]')
# driver2 = webdriver.Chrome()
# wait = wait.until(url2)
elem = driver.get(url2)
# elem = driver.find_element_by_xpath('//*[@id="zxnav_0"]/div[1]/a[1]/span')
elem = driver.find_element_by_xpath('//*[@id="4"]/div/div[2]/div[2]/a[1]')
elem.click()
# currentHandle = driver.getWindowHandles()
# driver.switchTo().window(currentHandle)
handles = driver.window_handles
for handle in handles:     # 切换窗口（切换到搜狗）
    if handle != driver.current_window_handle:
        # print('switch to', handle)
        driver.switch_to.window(handle)
        # print(driver.current_window_handle)    # 输出当前窗口句柄（搜狗）
        break
# driver.switch_to.window(handles[1])

html = driver.page_source
doc = PyQuery(html)
# doc('#pro-list clearfix')
items = doc('.pro-list .pro-panels').items()
try:
    conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test2', charset='utf8')
    cursor = conn.cursor()
    for item in items:
        # print(item.text())
        # print('===title====' + item('.p-img').children().attr('title'))
        # print('===src====='+item('.p-img').children().children().attr('src'))
        title = item('.p-img').children().attr('title')
        price = item('.p-price').children().text()
        img = item('.p-img').children().children().attr('src')
        name = item('.p-name').children().attr('title')
        detailhref = 'https://www.vmall.com' + item('.p-name').children().attr('href')
        comment = item('.p-button-score').children().text()
        values = (title, price, img, name, detailhref, comment)
        # cursor.executemany('INSERT INTO vmall(title,price,img,name,detailhref,comment) values('+title+','+price+','+img+','+name+','+detailhref+','+comment+')')
        cursor.execute('INSERT INTO vmall(title,price,img,name,detailhref,comment) values(%s,%s,%s,%s,%s,%s)', values)
        conn.commit()
except:
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
    driver.quit()






