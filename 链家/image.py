# coding: utf-8
"""
@python version : python3.10
@file name      : fj.py
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

save_data = []
df = pd.read_excel("house.xlsx")
for data in df.itertuples():
    save_data.append(list(data)[1:])

city_house_price_dict = {}
for info in save_data:
    city_name = info[0]
    house_unit_price = int(str(info[-1]).split('元')[0].replace(',', '').strip(''))
    if city_name not in city_house_price_dict:
        city_house_price_dict[city_name] = []
    city_house_price_dict[city_name].append(house_unit_price)

cit_avg_house_price = []
for k, v in city_house_price_dict.items():
    avg_price = round((sum(v) / len(v)), 2)
    cit_avg_house_price.append((k, avg_price))

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

mpl.rcParams["axes.unicode_minus"] = False
city_list = [item[0] for item in cit_avg_house_price]
avf_price = [item[1] for item in cit_avg_house_price]
# 创建数据集
x_pos = np.arange(len(city_list))
# 创建条形图


plt.bar(x_pos, avf_price,width=0.5)

# 显示数值
for i,v in enumerate(avf_price):
    plt.text(i,v,str(v),ha='center',va='bottom')
# 在x轴上创建名称
plt.xticks(x_pos, city_list)
plt.ylabel("房价(元)")
plt.title("浙江省城市平均房价")
# 显示图形
plt.legend()
plt.show()

