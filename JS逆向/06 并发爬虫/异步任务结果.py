# coding: utf-8
"""
@python version : python3.10
@file name      : 异步任务结果.py
@date           : 2024/3/13 17:03
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import time
import asyncio


async def task(i):
    print(f"任务{i}开始")
    await asyncio.sleep(i)
    print(f"任务{i}结束")
    return i * i


# 任务回调函数
def task2callback(ret):
    print("task2 的结果", ret.result())


start = time.time()
# 构建事件循环
loop = asyncio.get_event_loop()
# 协程对象任务列表 asyncio.ensure_future 可以获取返回结果
tasks = [
    asyncio.ensure_future(task(1)),
    asyncio.ensure_future(task(2)),
asyncio.ensure_future(task(3)),
]

# 当其中一个任务执行结束，回调函数
tasks[1].add_done_callback(task2callback)

# 如果没有执行结束则 asyncio.ensure_future(task(1)).done 为False
loop.run_until_complete(asyncio.wait(tasks))  # 阻塞等待所有任务结束
print(f"耗时:{time.time() - start}")
# 全部执行结束 打印返回值
for _task in tasks:
    print(_task.done(), _task.result())
