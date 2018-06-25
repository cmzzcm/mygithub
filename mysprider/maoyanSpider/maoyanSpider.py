#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.text)
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    # str1= '<dd>.*?board-index.*?>(\d+)</i>.*?board-img.*?src="(.*?)"</a>.*?<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd></p>.*?'
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-img.*?src="(.*?)"</a>.*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd></p>.*?', re.S)

    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-img.*?src="(.*?)"</a>.*?name"><a'
    #                      + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
    #                      + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',html, re.S)

    # \d 等价于 [0-9]
    # \d+ 表示至少一个数字，
    # .* 代表匹配除换行符之外的所有字符。
    # .*?  代表非贪婪模式，也就是说只匹配符合条件的最少字符
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>')
    items = re.findall(pattern, html)
    print(type(items))
    print(items[0])
    for item in items:
        yield {
            'index': item[0],
            # 'image': item[1],
            'title': item[1],
            # 'actor': item[2].strip()[2:],
            # 'time': item[3].strip()[4:],
            'actor': item[2],
            'time': item[3],
            'score': item[4]+item[5]
        }

def write_to_file(content):
    with open('resultd.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    main()


