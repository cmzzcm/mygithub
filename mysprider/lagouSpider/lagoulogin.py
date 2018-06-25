#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
import urllib.parse
import http.cookiejar
import json

# cookie设置
c = http.cookiejar.LWPCookieJar()
cookie = request.HTTPCookieProcessor(c)
opener = request.build_opener(cookie)

login_url = 'https://passport.lagou.com/login/login.json'
data = {
            'isValidate': 'true',
            'username': '15013410080',
            'password': '3192ad1ebd1ee4403ecaf63eabba4656',
            'request_form_verifyCode': '',
            'submit': ''
}
data = urllib.parse.urlencode(data).encode('utf-8')
req = request.Request(login_url)
req.add_header('Referer', 'https://passport.lagou.com/login/login.html?ts=1524907939327&serviceId=lagou&service=https%253A%252F%252Fwww.lagou.com%252F&action=login&signature=57BAD0171A0E6432AF6B1237EE03D0AB')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
resp = opener.open(req, data=data)
response = json.load(resp)
# print(resp.read().encode())
print(response)