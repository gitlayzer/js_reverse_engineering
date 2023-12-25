# coding: utf-8
"""
@python version : python3.10
@author         : ziyang.yang@aliyun.com
@describe       : 获取b站视频弹幕
"""
import re

import chardet
import requests
import json


# 比如获取此视频下所有的弹幕
# 首先查看视频的av号 ，比如BV1aW41187Qw 为视频编号，全站唯一

# https://api.bilibili.com/x/v1/dm/list.so?oid=XXX 这是哔哩哔哩弹幕数据接口，只需要获取对应的oid即可，下面将介绍如何获取对应的oid

# https://api.bilibili.com/x/player/pagelist?bvid=BV1EP4y1j7kV&jsonp=jsonp
# 将所需要的视频编号替换成此url的bvid 即可获取相应的数据,里面的cid 就是上述所需要的oid


def get_cid(video_num: str):
    """
    每个视频连接下可能有多个视频，这样就会获取多个cid，返回集合
    @param video_num:  视频编号,ex: BV1EP4y1j7kV
    @return: 弹幕所需要的oid
    """
    code = int
    url = f"https://api.bilibili.com/x/player/pagelist?bvid={video_num}&jsonp=jsonp"
    content = {}
    while code != 0:
        res = requests.get(url=url, timeout=None)
        data = json.loads(res.content.decode())
        code = data["code"]
        content = data

    cid_set = {item["cid"] for item in content["data"]}
    return cid_set  # {437626309, 437717574, 437729555, 437727348, 437659159, 437586584, 437550300}


def get_dm_data(oid):
    url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={oid}"
    flag = True
    dm_datas = {}
    while flag:
        res = requests.get(url=url, timeout=None)
        # 避免乱码操作
        res.encoding = chardet.detect(res.content)["encoding"]
        data = res.text.encode("gbk", "ignore").decode("gbk", "ignore")
        try:
            json.loads(data)
            flag = True
        except:
            flag = False
            # 正则处理数据，获取弹幕信息
            dm_datas["data"] = re.findall("<d.*?>(.*?)</d>", data, re.S)
    return dm_datas["data"]


if __name__ == "__main__":
    oid_list = get_cid("BV1aW41187Qw")
    # {28558760, 371495955, 53662198}
    for oid in oid_list:
        dm_data = get_dm_data(oid)
        for dm in dm_data:
            print(dm)
