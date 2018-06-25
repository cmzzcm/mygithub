#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests

def get_page_index():
    data = {
        'offset': 0,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None
    except RequestException:
        print('请求详情页面出错', url)
        return None

def main():
    html = get_page_index()
    print(html.encode().decode('unicode_escape'))

if __name__ == '__main__':
    main()
