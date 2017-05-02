#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/2 上午10:49
#@Author:grape.lee
#@File:py_04
#@Software:PyCharm Community Edition
'''购物车小程序'''
goods=[('cup',20),('mac',8000),('book',20),('bag',300),('milk',5),('car',120000)]
for i,j in enumerate(goods):
    print(i,j[0],j[1])
shop_car=[]
print("welcome".center(50, '-'))
salary = int(input("input your salary:"))
while True:
    goods_buy=int(input("what do you want to buy:\n"))
    price = goods[goods_buy][1]
    got_things=goods[goods_buy][0]
    if price < salary:
        shop_car.append(got_things)
        print("you had buy %s" % got_things)
        salary -= price
        continue
    else:
        print("你的余额不足")
        print("%s,你的余额是：%s" % (shop_car,salary))
        break
