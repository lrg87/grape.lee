#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/2 下午9:21
#@Author:grape.lee
#@File:py_09
#@Software:PyCharm Community Edition
'''
文件操作
'''
'''
f = open('file','模式')
r#只读模式
w#只写，先清空源文件
x#文件存在报错，不存在则创建文件并写内容。
b#二进制模式
a#追加模式

f = open('file','r')
data = f.read()
print(data)
f.close()
'''

'''
with open('user_file','r') as f:
    print(f.readlines())
'''

'''
f=open('user_file','r+')
#如果打开模式没有b，则read按照字符读取
data=f.read(1)
#tell告诉当前指针所在位置(字节)
print(f.tell())
#wirte在当前指针位置开始向后覆盖
f.write('888')
f.seek(3)
f.clise()



f.seek(3)
f.truncate()
截断seek点位之后的东西，并删除。
'''

with open('user_file','r') as f1,open('db1','a') as f2:
    pass

