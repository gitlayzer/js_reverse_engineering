# coding: utf-8
"""
@python version : python3.10
@file name      : websocket爬虫.py
@date           : 2024/3/27 9:27
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import websockets
import asyncio
import ssl
import certifi

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())


# https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml
async def main():
    url = "wss://hq.sinajs.cn/wskt?list=sh000001"
    # extra_headers给ws 传递请求头.
    async with websockets.connect(url, extra_headers={
        "Origin": "https://finance.sina.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }, ssl=ssl_context) as ws:
        await ws.send("")
        while True:
            ret = await ws.recv() # 等待接收消息
            print(ret)


if __name__ == '__main__':
    asyncio.run(main())