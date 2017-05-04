#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/2 下午8:15
#@Author:grape.lee
#@File:py_08
#@Software:PyCharm Community Edition
'''
内置函数
'''
'''
abs()
绝对值

any()
任一为真就为真

all()
所有为真才为真

bin()
2进制

oct()
8进制

hex()
16进制

bytes()
字符串转字节类型
'''
'''
#utf-8一个汉字是三个字节
#gbk一个汉字是二个字节
s='悟空'
n = bytes(s,encoding='utf8')
print(n)

字节转换成字符串
str(bytes('悟空',encoding='utf8'),encoding='utf8')
'''

#编译Python代码
#complie()

#exec()
'''只是执行没有执行结果，执行代码或字符串'''
#eval()
'''执行表达式并获取结果'''

'''
print(dir(list))
快速查看对象提供了那些功能

help(list)
查看详细用法
'''

# #分页功能
# r = divmod(100,9)
# print(r)
# print(r[0])
# print(r[1])
# 返回的数组，第一个元素是商，第二个元素是余数。

# 判断对象是否是类的实例
# s = 'haha'
# r = isinstance(s,str)
# print(r)


#filter,map
##fileter如果返回True,将元素添加到结果中
##map将函数返回值添加到结果中

#filter(函数，可迭代对象)
# def f1(a):
#     if a>22:
#         return True
# li=[11,22,33,44,55]
# ret=filter(f1,li)
# print(list(ret))
# #filter,循环第二个参数，让每个参数交给函数，如果函数返回True，加入ret


# f1=lambda a:a > 30
# rest=f1(90)
# print(rest)
# 返回结果是True


# li=[11,22,33,44,55]
# rest=filter(lambda a:a>30,li)
# print(list(rest))



# li=[11,22,33,44,55]
# def f1(args):
#     result=[]
#     for i in args:
#         result.append(i+10)
#     return list(result)
#
# ret=f1(li)
# print(list(ret))


# #map(函数，可迭代对象）
# li=[11,22,33,44,55]
# def f2(a):
#     return a +10
# result=map(f2,li)
# print(list(result))

# li=[11,22,33,44,55]
# result=map(lambda a:a+10,li)
# print(list(result))

# s='包拯'
# print(len(s))
#
# b=len(bytes(s,encoding='utf8'))
# print(b)
# python 2中len按照字节计算，python3中按照字符计算。

#反转
# li=[11,22,33,44]
# res=reversed(li)
# print(list(res))


# l1=['a',1,2,3]
# l2=['b',4,5,6]
# l3=['c',7,8,9]
# r=zip(l1,l2,l3)
# print(list(r))
