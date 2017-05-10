#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/9 下午4:07
#@Author:grape.lee
#@File:py_13
#@Software:PyCharm Community Edition



# import json
# dic1={'k1':'v1'}
# test1= json.dumps(dic1)
# print(test1,type(test1))
#json.dumps 将Python基本数据类型转换成字符串。


# s1='{"k1":123}'
# test2=json.loads(s1)
# print(test2,type(test2))
#json.loads 将字符串类型转换成基本的python数据类型。
#通过json.loads反序列化的时间一定用双引号""，不能使用单引号

# li=[11,22,33]
# json.dump(li,open('db','w'))
#json.dump将Python基本数据类型转换成字符串并写入文件


# li=json.load(open('db','r'))
# print(type(li),li)
#json.load读取文件并转换成python基本数据类型



#json/pickle
#json更加适合跨语言，字符串，基本数据类型
#pkicle,python所有类型的序列化，仅适用于Python，版本兼容性差。





