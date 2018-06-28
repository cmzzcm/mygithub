#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from random import randint

def pop():
    path = 'D:/python/scrapyProject/city58/city58/utils/proxy_swift/proxies.csv'
    df = pd.DataFrame(pd.read_csv(path, header=0))
    s = df.iloc[:, 0].size
    x = randint(0, s)
    proxy = df.loc[x][1]
    # print('----------------pop-ip-------------')
    # print(proxy)
    return proxy

# if __name__ == '__main__':
#     pop()