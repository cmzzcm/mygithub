#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import time


def get_user_data(page):
    user_data = []
    headers = {
        'cookie': 'aliyungf_tc=AQAAAELZ+H152AAANioZdLkcnRCudWfl; _xsrf=1d12d541-e162-46ee-a7fe-45cc51144576; d_c0="ALDv8nSWhQ2PTuBOaYH-UXC-auvONS81ZoQ=|1525083219"; _zap=ea771b49-ba08-41b8-81d7-c551067734af; l_n_c=1; n_c=1; l_cap_id="YWFlYTdiMTk4MTM2NGUwZTllMTI2MmVjNmQ3MDIyNjU=|1527848406|6f5c1e0136575f191bb582c36b6eb1c9a7efd4e5"; r_cap_id="NzYzMGYwNjEwOGI2NGYzYWFkYTc4M2RkMDZlYWVmMzc=|1527848406|0fd3649906a4e8879a9a472b866a0bd0b5c7ab6c"; cap_id="NDY1ZTg0ZWFjMmFmNGVmZjkxNTkyYTc2ODFkZDM1OWM=|1527848406|3b9d9af94d32584e7fb94bcafff7330eb3550181"; q_c1=3e294471bae6443eb85d103445a14149|1528727715000|1525237073000; tgw_l7_route=5bcc9ffea0388b69e77c21c0b42555fe; capsion_ticket="2|1:0|10:1528853544|14:capsion_ticket|44:MTY0ODQ4NmE3NDIwNDM2ZWE1NzVmYWQxODNhMjU5NzM=|c1e0a262ed0f41061596c530ab9f009848dbdcddf47af819b32ebdb1554b0fcc"; z_c0="2|1:0|10:1528853559|4:z_c0|92:Mi4xR3JzVUFRQUFBQUFBc09feWRKYUZEU1lBQUFCZ0FsVk5OOElOWEFBQ0U5OG5XNTdiSVhjaC1fOElXOGpWTHVDX3BB|eb0ff7725aea1c2af90f9fefe5ee729290eb9955eaa2e507271ce34872c32e7b"',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'x-udid': 'ALDv8nSWhQ2PTuBOaYH-UXC-auvONS81ZoQ=',
    }
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i * 20)
        r = requests.get(url, headers=headers).json()['data']
        user_data.extend(r)
        print('---------正在爬取第%d页------------' % (i+1))
        time.sleep(5)
    return user_data


if __name__ == '__main__':
    user_data = get_user_data(10)
    df = pd.DataFrame.from_dict(user_data)
    df.to_excel('zhihu.xlsx')