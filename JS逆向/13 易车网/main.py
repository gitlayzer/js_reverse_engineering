# coding: utf-8

# 获取某车型的配置信息，需要对请求头参数 做逆向解析

import requests
import json
import time
from hashlib import md5

# 获取配置的url
url = 'https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details'

# 在js代码中 X-Timestamp 为#        i["x-timestamp"] = t.timestamp，所以这个为时间戳

X_Timestamp = str(int(time.time())*1000)
param_str = json.dumps({"cityId":"2401","carIds":"170175", "serialId":"2714"},separators=(',',':'))
params = {
    'cid': '508',
    'param': param_str  # 去除序列化对 空格的使用
}

# 查看js 代码上X-sign的实现方式
"""
function s(e, t) {
            var n = "";
            if ("headers" == e.encryptType) {
                var i = e.data ? JSON.stringify(e.data) : "{}"
                  , o = r(e, t);
                n = "cid=" + t.cid + "&param=" + i + o + t.timestamp
            } else {
                var a = [];
                a.push("cid=" + t.cid),
                a.push("uid=" + t.uid),
                a.push("ver=" + t.ver),
                a.push("devid=" + (e.deviceId || "")),
                a.push("t=" + t.timestamp),
                a.push("key=" + t.paramsKey),
                n = a.join(";")
            }
            var s = yicheUtils.md5(n);
            return s
"""
# 由上面可知道 是通过 字符串拼接 然后进行md5转换得到一个字符串,其中19DDD1FBDFF065D3A4DA777D2D7A81EC 是pc端访问的固定值，也可以在js代码中查看
"""
19DDD1FBDFF065D3A4DA777D2D7A81EC 源代码位置

function i(e, t) {
            var n = {
                cid: "601",
                timestamp: (new Date).getTime(),
                gradeParam: {},
                uid: window.__uid__ || "",
                ver: window.__appver__ || null,
                headerEncryptKeys: [{
                    name: "pc",
                    value: "19DDD1FBDFF065D3A4DA777D2D7A81EC",
                    cid: "508"
                }, {
                    name: "phone",
                    value: "DB2560A6EBC65F37A0484295CD4EDD25",
                    cid: "601"
                }, {
                    name: "h5",
                    value: "745DFB2027E8418384A1F2EF1B54C9F5",
                    cid: "601"
                }, {
                    name: "business_applet",
                    value: "64A1071F6C3C3CC68DABBF5A90669C0A",
                    cid: "601"
                }, {
                    name: "wechat",
                    value: "AF23B0A6EBC65F37A0484395CE4EDD2K",
                    cid: "601"
                }, {
                    name: "tencent",
                    value: "1615A9BDB0374D16AE9EBB3BBEE5353C",
                    cid: "750"
                }],
                paramsKey: "f48aa2d0-31e0-42a6-a7a0-64ba148262f0"
            };
"""
# 前一部分是传入的参数,最后是时间戳
sign_str = f'cid=508&param={param_str}19DDD1FBDFF065D3A4DA777D2D7A81EC{X_Timestamp}'
md5_obj = md5()
md5_obj.update(sign_str.encode())
sign = md5_obj.hexdigest()

# 目前就剩X-User-Guid这个了 查看源代码 是一个随机字符串，如果没有登陆的话，如果登录的就取cookie一部分
# 针对没有登陆，可以执行原js代码获取
"""
function g() {
            return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                var t = 16 * Math.random() | 0
                  , n = "x" == e ? t : 3 & t | 8;
                return n.toString(16)
            })
        }
"""


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "X-City-Id": "2401",
    "X-Ip-Address": "139.226.104.22",
    "X-Platform": "pc",
    "X-Sign": sign,
    "X-Timestamp": X_Timestamp,
    "X-User-Guid": "3791e801-8bc7-4fe9-97d4-efa08a14f8c3"
}

print(sign,X_Timestamp)
res = requests.get(url=url, params=params, headers=headers)
print(res.text)
