# coding: utf-8
"""
@python version : python3.10
@file name      : 17k.py
@date           : 2024/3/13 10:48
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import os
import time

import requests
from lxml import etree

# 免费小说url
url = "https://www.17k.com/all/book/2_0_0_0_0_0_1_0_1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.17k.com/all",
    "Cookie": "GUID=8b93c880-1ee8-4ac7-a04d-c005b5eab968; BAIDU_SSP_lcr=https://www.baidu.com/link?url=rueuA7tyM3Eu2UmK9r6ffk5E4jYC7N7v09PGMQ7NsXi&wd=&eqid=ff9d19660008176b0000000465f11310; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1710297878; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228b93c880-1ee8-4ac7-a04d-c005b5eab968%22%2C%22%24device_id%22%3A%2218e35b28d26801-0d891a0e6ff854-26001b51-1327104-18e35b28d27f5d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=8cf9202517103056168613548e381c1296537d142258cff0ff21309aae; acw_sc__v2=65f13150bacb30c51b6369ff0b12f951c8c4c127; Hm_lpvt_9793f42b498361373512340937deb2a0=1710305629; tfstk=eGjJSEcj1SVo8lcwouUc8qOr5Tw0jgByG_WsxBAoRsCACOlkRUi79ZCCgUA7z62dM6C2Z3xWRsXflpNyOu-Cit_Xp7RQ4U_xpO5vx6BUUpOCO6dhrrqGUT-eA5bLjlXP9ZlAI52JBUl2YHNgilqGUT-F6KvSUGe6y566GiX56jpBaTOxvTSvFU3PFInIAinMyCiHMDiCDLIyGGjtRPcM6p07H-3E8U9qJ3IDVqTtQEpvs-0m828D3KdgH-3E8U92HC20m2ueoK5..; ssxmod_itna=Qq+xRDgDcD0nqBKGHD8Yb4m0KtG=KDBD2C=7hx05h+eGzDAxn40iDtooTPRYO07A2AWN0A7GvWhliOc2miSm+2WsbDCPGnDB9DqblYxii9DCeDIDWeDiDG4Gm94GtDpxG=Djjtz1M6xYPDEj5DRpPDuxBGDGP1LaKhDeKD0xTFDQ9hU2DDB20vQih5+PRGDiWFebypR=GEei08D7yhDlp4cR08T8dUQAvEU4kGEWKDXOQDvOvw21oDUBKsyPAN=ODPbnwYbA03Pe44W0xT7Y3NdOG5TQD4GAG53ihA7A1ZQDDWkC2HeYD===; ssxmod_itna2=Qq+xRDgDcD0nqBKGHD8Yb4m0KtG=KDBD2C=7xnKSD+5DsYhDLiioNeSrBRYqn4xOKBZkGQ3exzQOim/Qlq3Rz3v/dY4Iyb4=mFmzAPWxmjiL6Wx=Ykqki=beyShCFmny7NnKUpiO6mNW0KxR6DqecuiWaAiQE9DQOutQ4ywRl4wbpnQFguQd/T73mnAoOwvKpfw3ZnbQ+EdUSSftPmLh3BLVGfjKgT7czSUSSOX6Rvjy4ER+bjfqdQaZbcIWOniu8ZaeyWuaZabiL=2ipkH8r0t6Kepro9y7Ea9ir5HxKmZ68zB0fzVCu1GM8pTKmf8RD4Dn5KgGxnPyRk0RTbmkz8kql1OR+hd+Peoy8ThjkdgF7MzWDPD7jKGmtiqqAthGGKRDH9U7Kme7e4QDDjKDewx4D==="
}


# 获取小说标题，和详情页url
def get_title_url():
    info = []
    # 获取第一页得书名、小说详情页
    res = requests.get(url=url, headers=headers)
    # print(res.text)
    all_tree = etree.HTML(res.text)
    tr_list = all_tree.xpath("/html/body/div[4]/div[3]/div[2]/table/tbody/tr")
    for tr in tr_list:
        title = tr.xpath("td[3]/span/a/text()")
        detail_url = tr.xpath("td[3]/span/a/@href")
        if not title:
            continue
        info.append((title[0], detail_url[0]))
    return info


# 获取阅读页面url
def get_read_url():
    detail_info = get_title_url()
    every_chapter_info = []
    for item in detail_info:
        c_url = f"https:{item[1]}"
        res = requests.get(url=c_url, headers=headers)
        html_data = res.text
        d_tree = etree.HTML(html_data)
        _read_url = d_tree.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/dl/dt/a/@href")
        read_url = f"https://www.17k.com{_read_url[0]}"
        every_chapter_info.append((item[0], read_url))
        # print(item[0], c_url, _read_url)

    return every_chapter_info


# 获取详情页url下得章节url
def get_content_url():
    ret = get_read_url()
    content_dict = {}
    for item in ret:
        res = requests.get(item[1], headers=headers)
        chapter_html = res.text
        tree = etree.HTML(chapter_html)
        chapter_a_list = tree.xpath("/html/body/div[5]/dl/dd/a")
        content_dict.setdefault(item[0], [])
        for c_a in chapter_a_list:
            chapter_url = f"https://www.17k.com{c_a.xpath('@href')[0]}"
            chapter_title = c_a.xpath('text()')[0].strip()
            content_dict[item[0]].append((chapter_url, chapter_title))
    return content_dict


def save_local():
    import os
    content_data = get_content_url()
    for title, urls in content_data.items():
        print(title,urls)
        # if not os.path.exists(title):
        #     os.mkdir(title)
        # for item in urls:
        #     res = requests.get(url=item[0], headers=headers)
        #     with open(f"{title}/{item[1]}.txt", 'w', encoding='utf-8') as f:
        #         f.write(res.text)
        #     time.sleep(1)
        #     print(f"{title}/{item[1]}.txt 下载完成")


if __name__ == '__main__':
    save_local()
