#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/1/18 上午10:39
#@Author:grape.lee
#@File:get_goproxy_registry
#@Software:PyCharm Community Edition
import requests
import json
hlist=['xg-napos-order-1','xg-ecs-central-1']
url = ''
cookies= {}
'''requests的cookies格式是标准的字典格式，{"key1":"value","key2":"value"}'''
for i in hlist:
    print(i)
    req =requests.get(url+i,cookies=cookies)
    data=req.text
    '''print(data)'''
    a=json.loads(data)
    res=a[0]["regs"]
    for j in res:
        reg_appid=j["appid"]
        reg_cluster=j["cluster"]
        a=('{0}:{1}'.format(reg_appid,reg_cluster))
        print(a)
    print('#' * 50)
