# coding: utf-8
"""
@python version : python3.10
@file name      : 异步爬取斗图王图片.py
@date           : 2024/3/14 9:38
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import time

import requests
from lxml import etree
import asyncio
import aiohttp

# //div[@class="container_"]//div[@class="col-sm-9 center-wrap"]//img/@src
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


async def get_img_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.pkdoutu.com/article/list/', headers=headers) as response:
            tree = etree.HTML(await response.text())
            img_labels = tree.xpath('//div[@class="container_"]//div[@class="col-sm-9 center-wrap"]//img['
                                    '@data-backup]/@data-backup')
            file_info = [(item, item.split('/')[-1]) for item in img_labels]
            return file_info


async def download_url(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            with open(f"images/{file_name}", 'wb') as f:
                f.write(await response.content.read())
            print(file_name, '下载完成')


async def main():
    img_urls = await get_img_url()

    tasks = [asyncio.create_task(download_url(info[0], info[1])) for info in img_urls]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
