# coding: utf-8
"""
@python version : python3.10
@file name      : get_data.py
@date           : 2024/3/26 14:30
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import json

import requests
import execjs

# 获取cookies中的v值

with open('5.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
c_v = execjs.compile(js_code).call('resD.value')

# 请求数据

url = 'https://www.iwencai.com/customized/chart/get-robot-data'

data = {"source": "Ths_iwencai_Xuangu", "version": "2.0", "query_area": "", "block_list": "",
        "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
        "question": "今日涨停", "perpage": 50, "page": 1, "secondary_intent": "",
        "log_info": "{\"input_type\":\"click\"}", "rsh": "Ths_iwencai_Xuangu_ztv7i6fdyc8swi122d9bzajc5ismplup"}
headers = {
    "Content-Type": "application/json",
    "Cookie": f"other_uid=Ths_iwencai_Xuangu_ztv7i6fdyc8swi122d9bzajc5ismplup; ta_random_userid=x2s0ecscwn; cid=460366b4ae7bdfd11d0275b9e2ad9d0a1711427043; v={c_v}",
    "Hexin-V": c_v,
    "Referer": "https://www.iwencai.com/unifiedwap/result?tid=stockpick&qs=box_main_ths&w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

res = requests.post(url=url, json=data, headers=headers)
valid_data = json.loads(res.content.decode())
info = valid_data['data']['answer'][0]['txt'][0]['content']['components'][0]['data']['datas']
print(info)