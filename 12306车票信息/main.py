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

        return {v:k for k,v in stations.items()}

    # 获取车票信息
    def get_tickets(self):
        cookies = {
            '_uab_collina': '170666687428160801717765',
            'JSESSIONID': 'CB123B8FC643A51276467F1D90496133',
            'guidesStatus': 'off',
            'highContrastMode': 'defaltMode',
            'cursorStatus': 'off',
            '_jc_save_wfdc_flag': 'dc',
            'BIGipServerpassport': '820510986.50215.0000',
            'route': '6f50b51faa11b987e576cdb301e545c4',
            'BIGipServerotn': '2681667850.64545.0000',
            '_jc_save_fromDate': '2024-02-15',
            '_jc_save_toDate': '2024-02-15',
            '_jc_save_fromStation': '%u4E0A%u6D77%u8679%u6865%2CAOH',
            '_jc_save_toStation': '%u5F90%u5DDE%u4E1C%2CUUH',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '_uab_collina=170666687428160801717765; JSESSIONID=CB123B8FC643A51276467F1D90496133; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_wfdc_flag=dc; BIGipServerpassport=820510986.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=2681667850.64545.0000; _jc_save_fromDate=2024-02-01; _jc_save_toDate=2024-02-01; _jc_save_fromStation=%u4E0A%u6D77%u8679%u6865%2CAOH; _jc_save_toStation=%u5F90%u5DDE%u4E1C%2CUUH',
            'If-Modified-Since': '0',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5,AOH&ts=%E5%BE%90%E5%B7%9E%E4%B8%9C,UUH&date=2024-02-01&flag=N,N,Y',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'leftTicketDTO.train_date': '2024-02-15',
            'leftTicketDTO.from_station': 'AOH',
            'leftTicketDTO.to_station': 'UUH',
            'purpose_codes': 'ADULT',
        }

        response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryE', params=params, cookies=cookies,
                                headers=headers)
        tickets_list = response.json()['data']['result']
        valid_tickets = []
        stations_info = self.get_stations()
        for info in tickets_list:
            reg = re.compile(
                '.*?\|预订\|.*?\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*')
            result = re.findall('.*?\|预订\|.*?\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*', info)
            if len(result) > 0:
                valid_tickets.append(list(result[0]))
        header = ["车次", "出发站", "到达站", "出发时间", "到达时间", "历时", "商务座", "一等座", "二等座", "高级软卧",
                  "软卧", "动卧", "硬卧", "软座", "硬座", "无座"]
        print(header)
        for i in valid_tickets:
            if i[1] or i[2] in stations_info:
                i[1] = stations_info[i[1]]
                i[2] = stations_info[i[2]]
                print(i)


if __name__ == '__main__':
    ticket_obj = TicketsInfo()
    ticket_obj.get_tickets()
