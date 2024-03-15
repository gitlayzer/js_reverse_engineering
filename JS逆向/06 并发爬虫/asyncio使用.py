# coding: utf-8
"""
@python version : python3.10
@file name      : asyncio使用.py
@date           : 2024/3/13 16:59
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import time
import asyncio


# 老版本写法
# 3.5 3.6
async def task(i):
    print(f"任务{i}开始")
    await asyncio.sleep(i)
    print(f"任务{i}结束")


start = time.time()
tasks = [task(1), task(2)]  # 协程对象任务列表
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # 阻塞等待所有任务结束
print(f"耗时:{time.time() - start}")
