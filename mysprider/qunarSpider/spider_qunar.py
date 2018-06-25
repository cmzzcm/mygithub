#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
import re

def start_get_session():
    session_ = requests.session()
    return session_

def get_base_cookies(session_):
    session_.get('https://user.qunar.com/passport/login.jsp?')   # 获得QN1
    # response = session_.get('https://user.qunar.com/webApi/isNeedCaptcha.jsp')  # 获得QN1
    get_image(session_)  # 获得验证码图片
    session_.get('https://user.qunar.com/passport/addICK.jsp?ssl')
    # session_.get('https://rmcsdf.qunar.com/api/device/challenge.json?callback=callback_1526953867630&sessionId=116700e6-5687-4f2f-9798-5ce54c98e698&domain=qunar.com&orgId=ucenter.login')
        # '&sessionId=(.*?)&'

    response = session_.get('https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0')
    cookie_SE = re.findall(r'&sessionId=(.*?)&', response.text)[0]  #　找到session
    session_.get('https://rmcsdf.qunar.com/api/device/challenge.json?callback=callback_1526953867630&'
                 'sessionId={}&domain=qunar.com&orgId=ucenter.login'.format(cookie_SE))
    session_.cookies.update({'QN271': cookie_SE})  # 通过比对发现参数QN271和SESSIONID相同，所以直接加入cookies中

def get_image(session_):
    # src = "https://user.qunar.com/captcha/api/image?k={en7mni(z&amp;p=ucenter_login&amp;c=ef7d278eca6d25aa6aec7272d57f0a9a&amp;t=" + str(round(time.time() * 1000))
    response = session_.get(
        'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a'
        # 'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a&t=1526895762525'
        # 'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a&t=1526897954293'
        # src
          )
    with open('./img/code.png', 'wb') as f:
        f.write(response.content)  # 把二维码存进同级img文件夹下命名为code


def login(session_, username_, password_,code_):
    data = {
            'loginType': 0,
            'username': username_,
            'password': password_,
            'remember': 1,
            'vcode': code_,
    }
    url = 'https://user.qunar.com/passport/loginx.jsp'
    response = session_.post(url, data)
    print(response.text)
    res = session_.get('https://user.qunar.com/index/basic')
    print(res.text)


if __name__ == '__main__':
    session = start_get_session()
    get_base_cookies(session)
    username = input("请输入用户名：")
    password = input("请输入你的密码")
    code = input("请输入你的验证码")

    login(session, username, password, code)