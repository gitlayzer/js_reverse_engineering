import time
import hashlib

import requests

# 1.首页
res = requests.get(url="https://bbs.pku.edu.cn/v2/home.php")
cookie_dict = res.cookies.get_dict()

# 2.登录
user = "wupeiqi"
pwd = "123123"
ctime = int(time.time())
data_string = f"{pwd}{user}{ctime}{pwd}"

obj = hashlib.md5()
obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()

res = requests.post(
    url="https://bbs.pku.edu.cn/v2/ajax/login.php",
    data={
        "username": user,
        "password": pwd,
        "keepalive": "0",
        "time": ctime,
        "t": md5_string
    },
    cookies=cookie_dict
)

print(res.text)
