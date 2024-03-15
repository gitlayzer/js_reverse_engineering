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
import time
from lxml import etree
import re
import asyncio
import aiohttp

# 获取需要下载视频的 集数url

headers = {
    "Referer": "https://www.99meijutt.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


# 获取该电视剧每集的url地址
async def get_every_video_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.99meijutt.com/content/103548.html', headers=headers, ssl=False) as res:
            tree = etree.HTML(await res.text())
            li_list = tree.xpath('//*[@id="stab12"]/ul/li')
            video_info = [f"https://www.99meijutt.com{item.xpath('./a/@href')[0]}" for item in
                          li_list]
            return video_info


# 根据每集的url 获取第一个m3u8 url
async def get_first_m3u8_url(video_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(video_url, headers=headers, ssl=False) as res:
            _html = await res.text()
            tree = etree.HTML(_html)
            # 通过正则获取
            # 每一集的标题
            title = tree.xpath('/html/body/div/div[1]/div[1]/div[1]/div[1]/h1/text()')[0]
            first_m3u8_url = re.search('now="(.*?m3u8)"', _html).group(1)
            return first_m3u8_url, title  # https://v10.dious.cc/20240306/RK9EbMH6/index.m3u8


# 根据首个m3u8请求，获取带有ts url的m3u8请求url
async def get_ts_m3u8_url(first_m3u8_url, title):
    # 带有ts相应的url :https://v10.dious.cc/20240306/RK9EbMH6/2000kb/hls/index.m3u8
    async with aiohttp.ClientSession() as session:
        async with session.get(first_m3u8_url, headers=headers, ssl=False) as res:
            # 截取需要的url后缀
            _part_url = await res.text()
            part_url = _part_url.split('\n')[2].strip()
            # print(res)
            ts_m3u8_url = "https://v4.dious.cc" + part_url
            # get_ts_url(ts_m3u8_url, title)
            return ts_m3u8_url, title


async def get_ts_url(ts_m3u8_url, title):
    # https://v10.dious.cc/20240306/RK9EbMH6/2000kb/hls/IX9WCG3E.ts
    async with aiohttp.ClientSession() as session:
        async with session.get(ts_m3u8_url, headers=headers, ssl=False) as res:
            ts_ = re.findall('(/.*?.ts)', await res.text())
            ts_url_list = [f"https://v4.dious.cc{ts}" for ts in ts_]
            if not os.path.exists(title):
                os.mkdir(title)
            if not os.path.exists(f"{title}/ts"):
                os.mkdir(f"{title}/ts")
            with open(f"{title}/ts/index.m3u8", 'w', encoding='utf-8') as f:
                f.write(await res.text())
            return ts_url_list, title


# 下载ts 列表
async def download_ts(ts_url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(ts_url, headers=headers, ssl=False) as res:
            with open(f"{file_name}/ts/{ts_url.split('/')[-1].strip()}", 'ab') as f:
                f.write(await res.content.read())
            print(f"{file_name}/ts/{ts_url.split('/')[-1].strip()}下载完成")


async def download_video(video_url):
    f_m3ub_url, _title = await get_first_m3u8_url(video_url)
    ts_m3u8_url, title = await get_ts_m3u8_url(f_m3ub_url, _title)
    ts_urls, filename = await get_ts_url(ts_m3u8_url, title)

    tasks = [asyncio.create_task(download_ts(ts_url, filename)) for ts_url in ts_urls]

    await asyncio.wait(tasks)


def merge(filename):
    '''
    视频合并
    :return:
    '''
    # 进入到下载后ts 的目录
    os.chdir(f"{filename}/ts")
    # 视频合并的命令
    os.system(f'ffmpeg -i index.m3u8 -c copy {filename}/{filename}.mp4')
    print(f'视频{filename} 合并成功====')


async def main():
    f_m3ub_url, _title = await get_first_m3u8_url('https://www.99meijutt.com/play/15241-2-0.html')
    ts_m3u8_url, title = await get_ts_m3u8_url(f_m3ub_url, _title)
    ts_urls, filename = await get_ts_url(ts_m3u8_url, title)

    tasks = [asyncio.create_task(download_ts(ts_url, filename)) for ts_url in ts_urls]
    await asyncio.wait(tasks)
    # video_urls = await get_every_video_url()
    # tasks = [asyncio.create_task(download_video(url)) for url in video_urls]
    # await asyncio.wait(tasks)
    # merge(title)


if __name__ == '__main__':
    start = time.time()
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"总耗时:{time.time() - start}秒")
