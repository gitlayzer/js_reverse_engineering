# coding: utf-8
"""
@python version : python3.10
@file name      : 简单web应用程序.py
@date           : 2024/3/11 15:39
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : socket 简单应用
"""

import socket

sock = socket.socket()
sock.bind(("127.0.0.1",8888))
sock.listen(5)

print("server is running")

# 接受客户端发来的请求
conn,addr = sock.accept()
print('conn',conn)
print('addr',addr)
data = conn.recv(1024)
# 向客户端发送请求，BS模式需要遵循http协议
conn.send(b"HTTP/1.1 200 ok\r\n\r\nhello yang")
conn.close()
