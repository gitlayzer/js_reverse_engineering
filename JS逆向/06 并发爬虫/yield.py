# coding: utf-8
"""
@python version : python3.10
@file name      : yield.py
@date           : 2024/3/13 15:45
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""


# yield 迭代器和生成器 ：优化存储

def get_data():
    print('第一次存储')
    yield 1
    print('第二次存储')
    yield 2
    print('第三次存储')
    yield 3

def get_num():
    for i in range(1,100000):
        yield i

data = get_data() # 生成器对象<generator object get_data at 0x000001CDC75A4190>

nums = get_num()
for i in nums:
    print(i)