#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/6 下午11:19
#@Author:grape.lee
#@File:py_12
#@Software:PyCharm Community Edition
'''
装饰器
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能
'''
#@ + 函数名
#功能：1.自动执行outer函数并且将其下面的函数名f1当成参数传递
#功能：2.将outer函数的返回值，重新赋值给f1

# def outer(func):
#     return '111'
#
# def f1():
#     print('F1')

#不传参数
# def outer(func):
#     def inner():
#         print('before')
#         r = func()
#         print('after')
#         return r
#     return inner
#
# @outer
# def f1():
#     print('F1')

#f1()

###传递参数
# def outer(func):
#     def inner(a):
#         print('before')
#         r = func(a)
#         print('after')
#         return r
#     return inner
#
# @outer
# def f1(arg):
#     print(arg)
#
# f1('haha')

#传递多个参数的装饰器,使用王能参数。
# def outer(func):
#     def inner(*args,**kwargs):
#         print('before')
#         r = func(*args,**kwargs)
#         print('after')
#         return r
#     return inner
#
# @outer
# def f1(arg):
#     print(arg)


def outer(func):
    def inner():
        print('before')
        func()
        print('backend')
    return inner


@outer
def f1():
    print('你好')



