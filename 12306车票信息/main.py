# coding: utf-8
import requests
import re
from prettytable import PrettyTable
from selenium import webdriver
class TicketsInfo(object):
    def __init__(self):
        self.headers = {
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%BE%90%E5%B7%9E%E4%B8%9C,UUH&ts=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5,AOH&date=2024-01-31&flag=N,N,Y',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
        }

    # 获取车站名一级对应的代码
    def get_stations(self):
        params = {
            'station_version': '1.9297',
        }

        response = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js', params=params,
                                headers=self.headers)
        stations = dict(re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text))  # 提取车站名和简称
        print(stations)

    # 获取车票信息
    def get_tickets(self):
        pass


if __name__ == '__main__':
    ticket_obj = TicketsInfo()
    ticket_obj.get_stations()
