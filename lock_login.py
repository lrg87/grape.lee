#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/4/25 下午9:58
#@Author:grape.lee
#@File:py_03
#@Software:PyCharm Community Edition
'''
连续三次登录输入错误密码，锁定账户
'''
user_dic={'zhangsan':'123','lisi':'456','wangwu':'789'}
f = open('lock_file','r')
lockd_file = f.read()
f.close()
count = 0
for i in range(3):
    user_name = input("Please input your name:")
    user_pwd=input("Please input your password")
    if user_name in lockd_file:
        print('你已经被禁止登陆')
        break
    if user_name in user_dic.keys() and user_pwd == user_dic[user_name]:
        print("欢迎回来")
        break
    else:
        print("用户名密码输入错误")
        count +=1
        if count == 3 and user_name in user_dic.keys():
            with open('lock_file', 'a') as f:
                f.write(user_name)
        continue
