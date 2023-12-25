# coding: utf-8

import re
import pandas as pd
import requests
from lxml import etree
import threading

city_info = {'hz': '杭州', 'nb': '宁波', 'wz': '温州', 'jx': '嘉兴', 'huzhou': '湖州',
             'sx': '绍兴', 'jh': '金华', 'quzhou': '衢州', 'taizhou': '台州', 'yw': '义乌'}


# 获取第n页的 url

def get_zj_city_url_dict(pg):
    return {v: f"https://{k}.lianjia.com/ershoufang/pg{pg}" for k, v in city_info.items()}


def get_city_lis_label(_url):
    data_list = []
    # url = 'https://hz.lianjia.com/ershoufang/pg3/'
    url = _url[1]
    city_name = _url[0]
    resp = requests.get(url)
    html = resp.text.encode('gbk', 'ignore').decode('gbk')
    tree = etree.HTML(html)
    li_list = tree.xpath('//*[@id="content"]/div[1]/ul/li')
    data_list.append(li_list)
    data_list.append(city_name)
    return data_list


def get_house_data(li, city):
    title = li.xpath('div[1]/div[1]/a/text()')[0]
    detail_url = li.xpath('div[1]/div[1]/a/@href')[0]
    detail_html = requests.get(detail_url).text.encode('gbk', 'ignore').decode('gbk')
    date = re.findall('<span>(\d+-\d+-\d+)</span>', detail_html)[0]
    tree2 = etree.HTML(detail_html)
    try:
        area = tree2.xpath('/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[1]/text()')[0]

    except:
        area = tree2.xpath('/html/body/div[5]/div[2]/div[4]/div[2]/span[2]/a[1]/text()')[0]
    try:
        address = tree2.xpath('/html/body/div[5]/div[2]/div[5]/div[2]/a/text()')[0]
    except:
        address = tree2.xpath('/html/body/div[5]/div[2]/div[4]/div[2]/span[2]/a[2]/text()')[0]
    location = ''.join(li.xpath('div[1]/div[2]/div//text()')).replace(' ', '')
    house_info = li.xpath('div[1]/div[3]/div//text()')[0]
    tag = ','.join(li.xpath('div[1]/div[5]//text()'))
    total_price = li.xpath('div[1]/div[6]/div[1]/span/text()')[0] + '万'
    unit_price = li.xpath('div[1]/div[6]/div[2]/span/text()')[0]
    print(city, title, date, location,area,address,house_info, tag, total_price, unit_price)
    pd_data.append((city, title, location,area,address,house_info, tag, date, total_price, unit_price))


def get_urls():
    urls_info = []
    for i in range(10):
        res = get_zj_city_url_dict(i + 1)
        for k, v in res.items():
            urls_info.append([k, v])
    return urls_info


# 包含li标签 list和城市名
def get_data_list():
    total_data = []
    for _url_info in get_urls():
        # print(url_info)
        total_data.append(get_city_lis_label(_url_info))
    return total_data


if __name__ == '__main__':
    pd_data = []
    columns = ['城市', '标题', '小区名/位置', '所属区','详细地址','房屋信息', '标签', '挂牌时间', '总价', '单价']

    for i in get_data_list():
        t_join_list = []
        for li in i[0]:
            t = threading.Thread(target=get_house_data, args=(li, i[1]))
            t_join_list.append(t)
            t.start()
        for t in t_join_list:
            t.join()
            # get_house_data(li, i[1])
    df = pd.DataFrame(pd_data, columns=columns)
    # # 写入excel
    df.to_excel('house.xlsx', index=False,sheet_name="总数据")

