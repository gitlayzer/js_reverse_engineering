
# coding: utf-8
"""
@python version : python3.10
@author         : ziyang.yang@aliyun.com
@describe       :
所需的第三方库:
pip3 install requests
pip3 install movepy

执行代码前：
1.首先 登录B站，访问https://search.bilibili.com/all，打开F12 调试页面
2.刷新地址，Network一栏随便找一个web?开头的请求，复制Request Headers下的Cookie 值到下面get_response函数里的Cookie下
"""

import re
import json
import requests
from moviepy.editor import *
import asyncio


class BiMedias(object):
    def __init__(self, bv_num):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.bv = bv_num
        # 需要加上防盗链，否则访问失败
        self.headers = {
            "referer": "https://www.bilibili.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        }

    def get_response(self, url):
        return requests.get(url=url, headers=self.headers)

    # 获取标题 cid session
    def get_video_info(self):
        video_index_url = f"https://www.bilibili.com/video/{self.bv}"
        resp = self.get_response(video_index_url).text
        cid = re.findall('"cid":(\d+),', resp)[0]
        session = re.findall('"session":"(.*?)"', resp)[0]
        title = re.findall('<h1 title="(.*?)" class="video-title".*>', resp)[0]
        return cid, session, title

    # 获取音频的url
    def get_media_url(self):
        cid, session, title = self.get_video_info()
        play_url = "https://api.bilibili.com/x/player/playurl"
        params = {
            "cid": cid,
            "qn": "0",
            "type": "",
            "otype": "json",
            "fourk": "1",
            "bvid": self.bv,
            "fnver": "0",
            "fnval": "976",
            "session": session,
        }
        json_data = requests.get(
            url=play_url, params=params, headers=self.headers
        ).json()
        audio_url = json_data["data"]["dash"]["audio"][0]["baseUrl"]
        video_url = json_data["data"]["dash"]["video"][0]["baseUrl"]
        return audio_url, video_url, title

    # 保存音频数据到本地
    def save(self):
        audio_url, video_url, title = self.get_media_url()
        audio_content = self.get_response(audio_url).content
        video_content = self.get_response(video_url).content
        with open(f"{self.base_dir}/{title}.mp3", mode="wb") as f:
            f.write(audio_content)
        with open(f"{self.base_dir}/{title}.mp4", mode="wb") as f:
            f.write(video_content)
        return f"{self.base_dir}/{title}.mp3", f"{self.base_dir}/{title}.mp4", title

    # 音频合成
    def merge(self):
        try:
            audio_path, video_path, title = self.save()
            # 提取音轨
            audio = AudioFileClip(audio_path)
            # 读入视频
            video = VideoFileClip(video_path)
            # 将音轨合并到视频中
            video = video.set_audio(audio)
            # 输出
            video.write_videofile(f"{self.base_dir}/{title}(含音频).mp4")
            # 移除之前的音频信息
            os.remove(audio_path)
            os.remove(video_path)
            print(f"{title}下载完成,存储目录:{self.base_dir}/{title}(含音频).mp4")
        except Exception as e:
            print("合成失败", e)

    def run(self):
        self.merge()


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": "buvid3=0D0291A5-6CA1-1CB2-A09B-C96587DEA3EE80983infoc; b_nut=1676448780; _uuid=EA583A10C-754E-D106E-7B56-321046857867E82154infoc; buvid4=7F700708-B0C9-6F57-7C99-2EC67B63E9A482189-023021516-rO64Md6QzSJVFMDHDBVLLQ%3D%3D; rpdid=|(umYu~|~|mm0J'uY~YRR)~)Y; i-wanna-go-back=-1; header_theme_version=CLOSE; hit-new-style-dyn=0; hit-dyn-v2=1; LIVE_BUVID=AUTO4716767233026808; nostalgia_conf=-1; b_ut=5; CURRENT_PID=33cbb510-cf68-11ed-85e6-7b6f6c530bfb; FEED_LIVE_VERSION=V8; home_feed_column=5; enable_web_push=ENABLE; CURRENT_QUALITY=80; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; fingerprint=b08c660adf895d1d50666cf2672d5572; buvid_fp_plain=undefined; buvid_fp=9477b153865ac8012f0bc811b1528d5a; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDMyMTExNzYsImlhdCI6MTcwMjk1MTkxNiwicGx0IjotMX0._I59z6BBGMK7jayFU_seC05LFxosvRfZrf2oSUOmHnI; bili_ticket_expires=1703211116; bp_video_offset_83585115=877510154172497928; iflogin_when_web_push=0; innersign=0; b_lsid=F53528EA_18C8F0D60F7; browser_resolution=1536-372; SESSDATA=2f21e1b7%2C1718759222%2C6657d%2Ac1CjCWWuyK_-LgA9hV5_XsUL-o73j4GHWOS2clt2UwoVRmfAEdpoSOOyRaaw7Xaq5GZ1QSVjFkLXljbldZckVSYWNFdXdwUGxhSmM5RVc1TWszSnh3dnZpel9DdDloSUwyRFJ2RzRzdXd3N1lyQ245QXJZWmZfcmR5LXJfMmVuYzJLWVhVOXlUWjN3IIEC; bili_jct=0249246602835371faabc8233b47e9db; DedeUserID=83585115; DedeUserID__ckMd5=0150aaae3ba2b7e3; sid=f5qkgrom"
    }
    res = requests.get(url=url, headers=headers)
    key_data = json.loads(res.text.encode("gbk", "ignore").decode("gbk"))
    search_data = key_data["data"]["result"]
    return search_data


def get_video_info_list(url):
    for i in get_response(url):
        if i["result_type"] == "video":
            return i["data"]


# 获取一页的bv号
def get_bv_list(url):
    return [item["bvid"] for item in get_video_info_list(url)]


# 获取所有的bv号
def get_all_bvs(key_word):
    bvs = []
    for page in range(5):
        _url = f"https://api.bilibili.com/x/web-interface/wbi/search/all/v2?page={page + 1}&page_size=42&keyword={key_word}"
        for bv in get_bv_list(_url):
            bvs.append(bv)
    return bvs


async def download(bvNum):
    b = BiMedias(bvNum)
    b.run()


if __name__ == "__main__":
    keyword = input("请输入视频搜索关键字:")
    tasks = [download(bv) for bv in get_all_bvs(keyword)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
