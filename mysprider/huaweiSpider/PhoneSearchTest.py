#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery
import MySQLdb
import traceback
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


# 进入华为官网商城
def get_page(driver):
    elem = driver.find_element_by_xpath('//*[@id="kw"]')
    elem.send_keys("手机商城", Keys.ENTER)
    driver.implicitly_wait(30)  # 隐性等待，最长等30秒
    url2 = 'https://www.vmall.com'
    driver.get(url2)
    elem = driver.find_element_by_xpath('//*[@id="zxnav_0"]/div[1]/div/a/span')
    elem.click()
    handles = driver.window_handles  # 获得所有窗口句柄
    handle = handles[len(handles)-1]  # 获得最后一个窗口句柄
    driver.switch_to_window(handle)  # 切换到最后一个窗口
    return driver


# 翻页
def next_page(driver):
    try:
        wait = WebDriverWait(driver, 10)  # 设置等待
        site = ec.element_to_be_clickable((By.CSS_SELECTOR, '#page_ul > li.pgNext.link.next'))  # 找到下一页按钮
        submit = wait.until(site)
        submit.click()
        return driver
    except TimeoutException:
        print('异常了')
        return None


# 进入产品页
def get_product(driver, code):
    elem = driver.find_element_by_xpath('//*[@id="zxnav_{}"]/a/span'.format(code))
    elem.click()
    handles = driver.window_handles  # 获得所有窗口句柄
    handle = handles[len(handles)-1]  # 获得最后一个窗口句柄
    driver.switch_to_window(handle)  # 切换到最后一个窗口
    return driver


# 解析产品详情页面，并保存到数据库
def parse_page(driver):
    html = driver.page_source
    doc = PyQuery(html)
    items = doc('.pro-list .pro-panels').items()  # 定位到产品详情
    # 连接数据库
    con = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test2', charset='utf8')
    cur = con.cursor()
    try:
        for item in items:
            title = item('.p-img').children().attr('title')
            price = item('.p-price').children().text()
            img = item('.p-img').children().children().attr('src')
            name = item('.p-name').children().attr('title')
            href = 'https://www.vmall.com' + item('.p-name').children().attr('href')
            phone_id = ''.join(re.compile('product/(.*?).html', re.S).findall(href))
            comment = item('.p-button-score').children().text()
            value = (title, price, img, name, href, phone_id, comment)
            sql = "SELECT COUNT(*) FROM vmall WHERE phone_id = '%s'"  # 查询数据库是否存在数据
            cur.execute(sql % phone_id)
            result = cur.fetchone()[0]
            if result > 0:
                print('此型号手机已经存在！')
                # sql = "update vmall set name = 'lqp'"
            else:
                # 添加数据到数据库
                sql = 'INSERT INTO vmall(title,price,img,name,detailhref,phone_id,comment) values(%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sql, value)
                con.commit()
                print(name+phone_id+'//添加成功')
    except():
        traceback.print_exc()
        # 发生错误时会滚
        con.rollback()
        return None
    finally:
        # 关闭游标连接
        cur.close()
        # 关闭数据库连接
        con.close()
        return None


def main():
    driver = webdriver.Chrome()  # 打开goole浏览器
    driver.get('https://www.baidu.com')
    driver = get_page(driver)
    for code in range(0, 5):
        driver = get_product(driver, code)
        if code in range(2, 3):
            parse_page(driver)
        else:
            parse_page(driver)
            # 获得最大页数
            total = int(driver.find_element_by_xpath('//*[@id="pageTotal"]').get_attribute('value'))
            for page in range(1, total):
                driver = next_page(driver)   #翻页
                parse_page(driver)
    driver.quit()  # 退出浏览器
    return None


if __name__ == '__main__':
    main()