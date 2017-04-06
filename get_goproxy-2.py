#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/1/19 下午5:05
#@Author:grape.lee
#@File:get_goproxy_registry_file
#@Software:PyCharm Community Edition
import requests
import json
#hlist=['xg-napos-order-1','xg-ecs-central-1']
import requests
import json
#with open("file", "r")  as f:
#    hosts = [h.strip("\n") for h in f.readlines() if h != ""]


#hlist=['xg-napos-order-1','xg-ecs-central-1']
url = ''
cookies= {}
'''requests的cookies格式是标准的字典格式，{"key1":"value","key2":"value"}'''
hlist=open('host.txt','r')
for i in hlist.readlines():
    i = i.strip("\n")
    with open('goproxy.txt','a') as f:
        f.write(i + '\n')
        req =requests.get(url+i,cookies=cookies)
        data=req.text
        a=json.loads(data)
        if req.text == 'null':
            f.write('@' * 50 + '\n')
            continue
        res=a[0]["regs"]
        for j in res:
            reg_appid=j["appid"]
            reg_cluster=j["cluster"]
            m=('{0}:{1}'.format(reg_appid,reg_cluster))
            f.write(m + '\n')
            '''print(m)'''
        f.write( '#' * 50 + '\n' )
