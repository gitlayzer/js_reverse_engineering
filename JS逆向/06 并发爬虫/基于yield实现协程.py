# coding: utf-8
"""
@python version : python3.10
@file name      : 基于yield实现协程.py
@date           : 2024/3/13 15:53
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import time


def foo():
    print('foo start')
    yield
    print("foo stop")
    yield


def bar():
    print('bar start')
    yield
    print('bar stop')
    yield


gen_foo = foo()
gen_bar = bar()

start = time.time()
next(gen_foo)
next(gen_bar)
next(gen_foo)
next(gen_bar)
print(f"总耗时:{time.time()-start}")
