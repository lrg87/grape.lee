#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/9 下午11:48
#@Author:grape.lee
#@File:py_14
#@Software:PyCharm Community Edition
import time
import datetime
print(time.time())
#返回当前系统时间戳
print(time.ctime())
#返回当前系统时间
print(time.gmtime())
#将时间戳转换成struct_time格式
print(time.ctime(time.time() - 86400))
#将时间戳转换成一天前的字符串格式
print(time.gmtime(time.time() - 86400))
#将时间戳转换成一天前的struct_time格式
print(time.localtime())
#将时间戳转换成struct_time格式，返回本地时间
print(time.mktime(time.localtime()))
#将struct_time格式转换成时间戳格式
print(time.strftime("%Y-%m-%d %H:%M:%S"))
#将struct_time格式转换成指定字符串格式
print(time.strptime("2017-05-10","%Y-%m-%d"))
#将字符串格式转换成struct_time格式

print("datetime".center(40,'#'))
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()+datetime.timedelta(days=1))
