# coding: utf-8
"""
@python version : python3.10
@file name      : python_client.py
@date           : 2024/4/15 15:16
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import websockets
import asyncio


async def main():
    # python这边链接是为了什么? 为了让ws调用js. 完成加密
    # Python连接websocket服务器的逻辑
    async with websockets.connect("ws://127.0.0.1:8888/invoke.ws?name=iwencai") as ws:
        await ws.send("我是Python客户端！")  # 发送数据过去
        print("连接成功了")
        val = await ws.recv()
        print("核心value值:", val)


if __name__ == '__main__':
    asyncio.run(main())