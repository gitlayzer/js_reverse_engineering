# coding: utf-8
"""
@python version : python3.10
@file name      : webserver.py
@date           : 2024/4/15 15:19
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :  写一个接口调用
"""
from sanic import Sanic, HTTPResponse
import websockets
import asyncio
app = Sanic(__name__)

@app.route("/get")
async def func(req):
    # 在这里. 你可以接受参数. 指定哪个项目
    project_name = req.args.get("project_name")
    if project_name:
        async with websockets.connect(f"ws://127.0.0.1:8888/invoke.ws?name={project_name}") as ws:
            await ws.send("你好")  # 发送数据过去
            print("连接成功了")
            ret = await ws.recv()
        return HTTPResponse(ret)
    else:
        return HTTPResponse("至少要给我一个project_name")


if __name__ == '__main__':
    app.run()
