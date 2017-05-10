#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#@Time:2017/5/4 下午2:28
#@Author:grape.lee
#@File:py_11
#@Software:PyCharm Community Edition
'''
n= json.loads(s)#将一个字符串转换成Python的基本数据类型；注意：字符串内部的字符串必须是用双引号扩着。
'''

def fetch(backend):
    registry_list = []
    with open('ha.conf','r') as f:
        flag = False
        for line in f:
            if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith('backend'):
                flag = False
                break
            if flag and line.strip():
                registry_list.append(line.strip())
    #print(registry_list)
    return registry_list

#fetch('buy.oldboy.org')

def add(backend,registry):
    result = fetch(backend)
    print(result)
    if not result:
        with open('ha.conf','r') as old,open('new.conf','w') as new:
            for old_line in old:
                new.write(old_line)
            new.write("\nbackend " +backend +'\n')
            new.write(''*8 + registry + '\n')
            '''这里要跳出循环，否则跟循环一块迭代进文件了。
            和for在同一级别，fow完成后才会写入最后不存在的行。'''
    else:
        #backend 存在，registry存在
        if registry in result:
            import shutil
            shutil.copy('ha.conf','new.conf')
        else:
            #backend存在，registry不存在
            result.append(registry)
            print(result)
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        print(line)
                        for tmp in result:
                            new.write(" "*8 + tmp + '\n')#' '表示空格里边要留空。
                            print(tmp)
                        continue#continue判断加在这里
                    if flag and line.strip().startswith('backend'):
                        flag = False
                        #new.write(line)
                        #print(line)
                        #continue
                    if line.strip() and not flag:
                        new.write(line)
                        print(line,'test-1')
                     #   print('你好')

bk="www.oldboy.org"
rg="server 101.31.11.9 101.31.11.9 weight 20 maxconn 340"

t = fetch(bk)
print(t)
add(bk,rg)
