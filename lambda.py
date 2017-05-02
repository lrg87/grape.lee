#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/2 下午7:51
#@Author:grape.lee
#@File:py_07
#@Software:PyCharm Community Edition
'''
lambda表达式，是简单函数的另一种实现方式
'''
def f1(a1):
    print(a1+100)
    
res1 = f1(10)


f2 = lambda a1:a1 + 100
res2 = f2(10)
print(res2)
