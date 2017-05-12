#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/12 下午3:53
#@Author:grape.lee
#@File:py-16
#@Software:PyCharm Community Edition
import time,sys

def view_bar(num,total):
    rate = num / total
    rate_num = int(rate * 100)
    ret = ("\r%s=>%d%%" % ('#'*num,rate_num))
    sys.stdout.write(ret)


for i in range(0,101):
    time.sleep(0.1)
    view_bar(i,101)
