# coding: utf-8
"""
@python version : python3.10
@file name      : wencai.py
@date           : 2024/4/15 15:20
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :  程序入口函数
"""
import execjs
import requests
import json

url = "http://127.0.0.1:8000/get?project_name=iwencai"
v = requests.get(url).text
print("核心V：", v)

url = "http://www.iwencai.com/customized/chart/get-robot-data"
data = {
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
    "question": "昨日涨停",  # 关键字
    "perpage": "100",
    "page": 1,
    "secondary_intent": "",
    "log_info": "{\"input_type\":\"click\"}",
    "rsh": "Ths_iwencai_Xuangu_3yuob5w3o4dvrcbhsw12iqjy7gjguq1g"
}
headers = {
    "Content-Type": "application/json",
    "Cookie": f"other_uid=Ths_iwencai_Xuangu_3yuob5w3o4dvrcbhsw12iqjy7gjguq1g; ta_random_userid=mfs8usg5z9; cid=65bd32be32c872afb291f11ff174681f1685011796; v={v}",
    "hexin-v": v,
    "Origin": "http://www.iwencai.com",
    "Referer": "http://www.iwencai.com/unifiedwap/result?w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
res = requests.post(url, data=json.dumps(data), headers=headers)
print(res.text)
