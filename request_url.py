#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2016/11/9 下午3:47
#@Author:grape.lee
#@File:requests_url
#@Software:PyCharm Community Edition
import sys
import json
# sys.path.append('/Library/Python/2.7/site-packages')
sys.path.append('/Library/Python/2.7/site-packages')
import requests

url = 'http://pms.elenet.me/pmo.api/module/syncall'
r = requests.get(url)
r.encoding = 'utf-8'
with open('url_file.json','w',encoding = 'utf8') as f:
    f.write(r.text)
key_list=('organizationName','moduleStatus','critical','moduleOwner','departmentName','appId')
print(key_list)
things = input('please input your search things:')
things_value = input('please input your things value:')
with open('url_file.json', 'r') as j:
    data = json.load(j)
    for i in data.get('resultMsg', []):
        if i[things] == things_value:
            print("%s" % i)
