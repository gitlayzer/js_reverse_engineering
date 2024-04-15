# coding: utf-8
"""
@python version : python3.10
@file name      : ws_server.py
@date           : 2024/4/15 15:14
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :  中间商操作
"""
import websockets
import asyncio
import re

browser_info = {}
client_info = {}


# 第一个参数ws表示服务器与客户端的链接
# path表示请求过来的路径
async def handle(ws_client, path):
    # 建立连接的时候走这里.
    # /register.ws?name=iwencai => 浏览器那边
    # /invoke.ws?name=iwencai => python客户端那边

    # 解析path
    print("path::", path)
    obj = re.compile(r"/(?P<action>.*?)\.ws\?name=(?P<name>.*)")
    search_result = obj.search(path)
    action = search_result.group("action")
    name = search_result.group("name")

    # 注册ws对象
    if action == "register":  # 来自浏览器
        browser_info[name] = ws_client  # 保存该链接
        print("浏览器连接成功！")
    elif action == 'invoke':
        client_info[name] = ws_client
        print("Python客户端连接成功！")
    else:
        print("客户端类型错误！")

    # 中转消息
    async for msg in ws_client:
        print("msg:::", msg)
        if action == "register":
            # 接受到的消息来自于浏览器
            await client_info[name].send(msg)
        elif action == "invoke":
            await browser_info[name].send(msg)


async def main():
    # 启动websocket服务区
    async with websockets.serve(handle, "127.0.0.1", 8888) as ws_server:
        print("你成功的启动了一个websocket")
        await asyncio.Future()  # 永远停在这里.


if __name__ == '__main__':
    asyncio.run(main())