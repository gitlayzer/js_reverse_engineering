# coding: utf-8
"""
@python version : python3.10
@file name      : 线程池.py
@date           : 2024/3/13 15:08
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print(f'任务{i}开始！')
    time.sleep(i)
    print(f'任务{i}结束！')
    return i


pool = ThreadPoolExecutor(3)

start = time.time()
future_list = []
for i in range(10):
    future = pool.submit(task, i + 1)
    future_list.append(future)
pool.shutdown()
print(f"总耗时:{time.time() - start}")

res = [future.result()for future in future_list]
print(res)
