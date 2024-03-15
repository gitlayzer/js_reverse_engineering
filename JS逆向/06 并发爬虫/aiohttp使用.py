# coding: utf-8
"""
@python version : python3.10
@file name      : aiohttp使用.py
@date           : 2024/3/14 9:35
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async  with session.get("http://httpbin.org/headers") as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.run(main())
