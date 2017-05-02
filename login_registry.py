#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/2 下午12:35
#@Author:grape.lee
#@File:py_05
#@Software:PyCharm Community Edition
'''
函数式登录、注册
'''
def login(username,password):
    '''
    :param username: 用户名
    :param password: 密码
    :return: 用户名、密码正确返回True,否则False
    '''
    with open('user_file','r') as f:
        for line in f.readlines():
            if line.strip().split('|')[0] == username and line.strip().split('|')[1] == password:
                print('welcome to login')
                return True
        return False
    f.close()


def registry(username,password):
    with open('user_file','a') as f:
        f.write('\n' + username + '|' + password)
        f.close()


def main():
    t = input("1:login;2:registry\n")
    if t == '1':
        username = input("please input your name:")
        password = input("please input your pwd:")
        tmp = login(username,password)
        if tmp == True:
            print("登录成功")
        else:
            print("登录失败")
    elif t == '2':
        print("注册")
        username = input("please input your name:")
        password = input("please input your pwd:")
        registry(username,password)
if __name__ == '__main__':
    main()
