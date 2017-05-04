#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/4 下午1:17
#@Author:grape.lee
#@File:py_10
#@Software:PyCharm Community Edition
'''
random 模块练习
ascii a~z,对应97-122；A~Z,对应65-91
数字不能使用jion方法需要转换成字符串模式。
'''

import random
'''
import random
r=random.randrange(10)
print(r)
'''

'''
r=random.random()
print(r)
'''

li=[]
for i in range(5):
    r =  random.randrange(5)
    if r == 1 or r == 3:
        tmp = random.randrange(0,10)
        li.append(str(tmp))
    else:
        tmp = random.randrange(97,123)
        h = chr(tmp)
        li.append(h)

result = "".join(li)
print(result)
