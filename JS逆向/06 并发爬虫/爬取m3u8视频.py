# coding: utf-8
"""
@python version : python3.10
@file name      : 爬取m3u8视频.py
@date           : 2024/3/14 11:03
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :
"""
import os.path

import requests
from lxml import etree
import re
# 获取需要下载视频的 集数url

session = requests.session()
headers = {
    "Referer": "https://www.99meijutt.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


# 获取该电视剧每集的url地址
def get_every_video_url():
    res = session.get('https://www.99meijutt.com/content/103548.html', headers=headers, verify=False)
    tree = etree.HTML(res.text)
    li_list = tree.xpath('//*[@id="stab12"]/ul/li')
    video_info = [f"https://www.99meijutt.com{item.xpath('./a/@href')[0]}" for item in
                  li_list]
    return video_info


# 根据每集的url 获取第一个m3u8 url
def get_first_m3u8_url(video_url):
    res = session.get(video_url, headers=headers, verify=False)
    _html = res.text
    tree = etree.HTML(_html)
    # 通过正则获取
    # 每一集的标题
    title = tree.xpath('/html/body/div/div[1]/div[1]/div[1]/div[1]/h1/text()')[0]
    first_m3u8_url = re.search('now="(.*?m3u8)"', _html).group(1)
    return first_m3u8_url, title  # https://v10.dious.cc/20240306/RK9EbMH6/index.m3u8


# 根据首个m3u8请求，获取带有ts url的m3u8请求url
def get_ts_m3u8_url(first_m3u8_url, title):
    # 带有ts相应的url :https://v10.dious.cc/20240306/RK9EbMH6/2000kb/hls/index.m3u8
    res = session.get(first_m3u8_url, headers=headers, verify=False)
    # 截取需要的url后缀
    part_url = res.text.split('\n')[2].strip()
    # print(res)
    ts_m3u8_url = "https://v10.dious.cc" + part_url
    get_ts_url(ts_m3u8_url, title)


def get_ts_url(ts_m3u8_url, title):
    # https://v10.dious.cc/20240306/RK9EbMH6/2000kb/hls/IX9WCG3E.ts
    res = session.get(ts_m3u8_url, headers=headers, verify=False)
    ts_ = re.findall('(/.*?.ts)', res.text)
    ts_url_list = [f"https://v10.dious.cc{ts}" for ts in ts_]
    if not os.path.exists(title):
        os.mkdir(title)
    # print(title,ts_url_list)
    return ts_url_list


def download_ts(ts_url, file_name):
    res = session.get(ts_url, headers=headers, verify=False)
    with open(f"{file_name}/{file_name}.mp4", 'ab') as f:
        f.write(res.content)


if __name__ == '__main__':
    for i in get_every_video_url():
        f_m3ub_url, _title = get_first_m3u8_url(i)
        get_ts_m3u8_url(f_m3ub_url, _title)
