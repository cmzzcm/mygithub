#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
from urllib import request
import pandas as pd
import json
import requests
from pymongo import MongoClient
import MySQLdb as mdb
from fake_useragent import UserAgent

def save_to_mogodb(posithon_data):
    client = MongoClient()
    db = client.test
    my_set = db.set
    my_set.insert(posithon_data)

def save_to_csv(position_data):
    df = pd.DataFrame.from_dict(position_data)
    df.to_csv('lagouposithon.csv', encoding='utf_8')
    # df.to_excel('lagou.xlsx')

def get_page_detail(url, page_headers, page_data):
    # req = urllib.request.Request(url, headers=page_headers)
    # position_data = request.urlopen(req, data=page_data.encode('utf-8')).read().decode('utf-8')
    position_data = requests.post(url, data=page_data, headers=page_headers)
    return position_data

def main():
    print('============main,ok=========')
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
    page_headers = {
        'User-Agent': UserAgent.random(),
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        # 'Connection': 'keep-alive',
        # 'Host': 'www.lagou.com',
        # 'Origin': 'https://www.lagou.com',
        'Cookie': 'WEBTJ-ID=20180514133943-1635d296420243-0709046ffe36ec-3f3c5501-1049088-1635d2964211db; _ga=GA1.2.1103456409.1526276384; user_trace_token=20180514133948-371bc43d-5739-11e8-8246-5254005c3644; LGUID=20180514133948-371bc89b-5739-11e8-8246-5254005c3644; JSESSIONID=ABAAABAAADEAAFIC9649D1BB9E2C2296415BE2F82487ABC; index_location_city=%E6%B7%B1%E5%9C%B3; X_HTTP_TOKEN=03d4c483d999a45a3d3a5bc8811d46d1; gate_login_token=""; LG_LOGIN_USER_ID=""; _gid=GA1.2.768244742.1528876534; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=28; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527928860,1528876885; LGSID=20180613163629-de4088d8-6ee4-11e8-9512-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%25E5%25AE%259E%25E4%25B9%25A0%3Foquery%3Dpython%26fromSearch%3Dtrue%26labelWords%3Drelative%26city%3D%25E6%25B7%25B1%25E5%259C%25B3; login=false; unick=""; _putrc=""; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528879585; LGRID=20180613164627-42ee8eab-6ee6-11e8-9512-5254005c3644; TG-TRACK-CODE=index_search; SEARCH_ID=472dcc6ab0974b6e84e16f9d031dab64',
        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        # 'X-Requested-With': 'XMLHttpRequest',
    }
    # # 设置post参数
    # page_num = 1
    # keywords ='python'
    # page_data = urllib.parse.urlencode([
    #     ('pn', page_num),
    #     ('kd', keywords)
    # ])
    pn = 18
    kd = 'python'
    for i in pn:
        page_data = {
            'first': 'true',
            'pn': i,
            'kd': kd,
        }

        response = get_page_detail(url, page_headers, page_data)
        position_data = response.json()['content']['positionResult']['result']
        save_to_csv(position_data)
        # save_to_mogodb(position_data)
        print(position_data)

if __name__ == '__main__':
    main()