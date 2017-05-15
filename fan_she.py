#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/15 下午3:59
#@Author:grape.lee
#@File:py_18
#@Software:PyCharm Community Edition

'''
用字符串代替函数
'''

'''
#模块在程序目录下边的情况。
import py_17

def run():
    inp = input('请输入你要访问的页面:\n')
    if hasattr(py_17,inp):
        func = getattr(py_17,inp)
        func()
    else:
        print('404'.center(10,'-'))


if __name__ == '__main__':
    run()

'''




'''
#不同的函数分布在不同的模块内部的情况下的反射
def run():
    inp = input('请输入你要访问的页面:\n')
    m,f = inp.split('/')
    obj = __import__(m)
    if hasattr(obj,f):
        func = getattr(obj,f)
        func()
    else:
        print('404'.center(10,'-'))


if __name__ == '__main__':
    run()
'''


