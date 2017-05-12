#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/12 上午11:50
#@Author:grape.lee
#@File:py_16
#@Software:PyCharm Community Edition

'''
使用递归方式实现阶乘
'''

def func(num):
    if num == 1:
        return 1
    return num * func(num - 1)


print(func(5))

'''
实现过程
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
'''
