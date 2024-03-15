# coding: utf-8
"""
@python version : python3.10
@file name      : 互斥锁.py
@date           : 2024/3/13 14:50
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import time
import threading

x = 100
lock = threading.Lock()


def sub():
    lock.acquire()  # 加锁
    global x
    tmp = x - 1
    time.sleep(0.05)
    x = tmp
    lock.release()  # 释放锁


# 串行写法
# for i in range(100):
#     sub()
# print(x)  # 0

# 并行写法
t_join_list = []
for i in range(100):
    t = threading.Thread(target=sub)
    t_join_list.append(t)
    t.start()
for t in t_join_list:
    t.join()

print(x)  # 数据不确定，多线程导致数据不一致

# 互斥锁
