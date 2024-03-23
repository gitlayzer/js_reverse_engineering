# coding: utf-8
import requests
import json
import execjs


# js代码最终执行加密请求体数据的入参值
def get_encrypt_strings(song_id):
    # js加密参数函数中是由第一个是变量，其他参数都是固定值
    decrypt_param_1 = json.dumps({"ids": f"[{song_id}]", "level": "standard", "encodeType": "aac", "csrf_token": ""})
    decrypt_param_2 = '010001'
    decrypt_param_3 = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    decrypt_param_4 = '0CoJUm6Qyw8W8jud'

    return decrypt_param_1, decrypt_param_2, decrypt_param_3, decrypt_param_4


# 获取请求体的加密数据
def get_post_encrypt_data(song_id):
    encrypt_strings = get_encrypt_strings(song_id)
    with open('crypt_params.js', 'r', encoding='utf-8') as f:
        JS_code = f.read()
    encrypt_params = execjs.compile(JS_code).call('encrypt_params', *encrypt_strings)

    # print(encrypt_params)
    # {'encText': 'HhIVl+fALBLv8SajA4I9dgh3knqmHH42WuoqkyvSAutrB8sEpM34ZkTJQQkjLu8mI83NLBiOtIjAFd5t/p3ch1r+sV7Ei+1lEdCPIAsh//QSNvVAbwVQUbbEx9i4/QtmtH080tGiO/tAHtZr5bAEiV1ttgPfbQiEDKVhpvFnyIvBYss6nv1iosGDs84wUjfj', 'encSecKey': '5994a62c6b992ccdc2c2d443e7a46c9836c5b80bf36ccb7e5ea783ba1a320a6a399693164d62b4023d76957becaf0e9c047d0310a16bdc0f31f98444451dc305727c5e6a798d1a5e876b2486a10dd3078fb2248d45d4e3a7be15002264d331fbe2e664801e10456282db37971d3f655d103e54d5c8bc8623b1fe03337d93c78e'}
    return encrypt_params


def get_song_download_url(song_id):
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://music.163.com/'
    }
    js_data = get_post_encrypt_data(song_id)
    # 通过JS获取的数据，进行请求体数据构造
    data = {
        'params': js_data.get('encText'),
        'encSecKey': js_data.get('encSecKey')
    }
    response = requests.post(url=url, headers=headers, data=data)

    song_download_url = json.loads(response.content.decode())['data'][0]['url']

    return song_download_url


def download(song_id):
    d_url = get_song_download_url(song_id)
    res = requests.get(url=d_url)
    print(f"开始下载{song_id}.m4a...")
    with open(f'{song_id}.m4a', 'wb') as f:
        f.write(res.content)

    print(f"{song_id}.m4歌曲下载完成")


if __name__ == '__main__':
    songId = input('请输入需要下载的歌曲ID>>>>>>>: ').strip()
    download(songId)
