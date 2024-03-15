# coding: utf-8
"""
@python version : python3.10
@file name      : 异步协程新版本新写法.py
@date           : 2024/3/14 9:23
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

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


async def main():
    tasks = [
        asyncio.ensure_future(task(1)),
        asyncio.ensure_future(task(2)),
        asyncio.ensure_future(task(3)),
    ]
    # 获取异步任务结果
    # res = await asyncio.gather(tasks[0], tasks[1], tasks[2])
    res = await asyncio.gather(*tasks)
    print(res)
    # await asyncio.wait(tasks)


start = time.time()
asyncio.run(main())
print(f"耗时:{time.time() - start}")
