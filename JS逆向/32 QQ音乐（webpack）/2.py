# coding: utf-8
"""
@python version : python3.10
@file name      : 2.py
@date           : 2024/4/9 17:11
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests

import execjs

with open("QQ.js",encoding='utf-8') as f:
    js_code = f.read()

js_compile = execjs.compile(js_code)

cookies = {
    'pgv_pvid': '9635345475',
    'RK': 'tHu9YFncEc',
    'ptcz': '1bf651c1965d9556fb90da8520e56a8df88556d9a6fe55f882ee313e8fd24502',
    'pac_uid': '1_916852314',
    'iip': '0',
    'pgv_info': 'ssid=s4057219154',
    'fqm_pvqid': 'd6000483-669d-4078-ae72-bf1cc85fcd8e',
    'fqm_sessionid': '913c138b-cc2a-4a43-93e1-c05a90dc5198',
    'ts_refer': 'www.baidu.com/link',
    'ts_uid': '1734036000',
    'psrf_access_token_expiresAt': '1706520186',
    'music_ignore_pskey': '202306271436Hn@vBj',
    'o_cookie': '916852314',
    'psrf_qqaccess_token': '',
    'qm_keyst': 'W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8',
    'tmeLoginType': '1',
    'psrf_qqopenid': '',
    'qqmusic_key': 'W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8',
    'wxopenid': 'opCFJw7mQbWsbTZY-6APJ3sDpOog',
    'euin': 'oK6kowEAoK4z7Kns7wci7eo5ov**',
    'qm_keyst': 'W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8',
    'wxrefresh_token': '74_MvFzomPrUECMq1Fubk1FriD42Zy8Wc0yBLz_kHOb_Wr7QFC4a-_u09VDvzIksSi5xEoY_X1x3iXFUIM6N6ZShWycIVY0rXRPx_nOoAHJ_5k',
    'wxuin': '1152921505066834311',
    'psrf_qqrefresh_token': '',
    'wxunionid': 'oqFLxsgoo1hMWdjTPFEd0Eo8Xb54',
    'psrf_qqunionid': '',
    'wxuin': '1152921505066834311',
    'login_type': '2',
    'ts_last': 'y.qq.com/',
}

headers = {
    'authority': 'u.y.qq.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'pgv_pvid=9635345475; RK=tHu9YFncEc; ptcz=1bf651c1965d9556fb90da8520e56a8df88556d9a6fe55f882ee313e8fd24502; pac_uid=1_916852314; iip=0; pgv_info=ssid=s4057219154; fqm_pvqid=d6000483-669d-4078-ae72-bf1cc85fcd8e; fqm_sessionid=913c138b-cc2a-4a43-93e1-c05a90dc5198; ts_refer=www.baidu.com/link; ts_uid=1734036000; psrf_access_token_expiresAt=1706520186; music_ignore_pskey=202306271436Hn@vBj; o_cookie=916852314; psrf_qqaccess_token=; qm_keyst=W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8; tmeLoginType=1; psrf_qqopenid=; qqmusic_key=W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8; wxopenid=opCFJw7mQbWsbTZY-6APJ3sDpOog; euin=oK6kowEAoK4z7Kns7wci7eo5ov**; qm_keyst=W_X_5gyyGR2l6P0dmU8bx4kt0aPOI83Jjbeo3ryTD12OTeuZIaVO9LVaNG6HvxtNwyx0Jxurd8otqrU8; wxrefresh_token=74_MvFzomPrUECMq1Fubk1FriD42Zy8Wc0yBLz_kHOb_Wr7QFC4a-_u09VDvzIksSi5xEoY_X1x3iXFUIM6N6ZShWycIVY0rXRPx_nOoAHJ_5k; wxuin=1152921505066834311; psrf_qqrefresh_token=; wxunionid=oqFLxsgoo1hMWdjTPFEd0Eo8Xb54; psrf_qqunionid=; wxuin=1152921505066834311; login_type=2; ts_last=y.qq.com/',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505066834311","g_tk_new_20200303":1799252052,"g_tk":1799252052},"req_1":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"33844389614678453","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_2":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"34959302995177909","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_3":{"module":"MessageCenter.MessageCenterServer","method":"GetMessage","param":{"uin":"1152921505066834311","red_dot":[{"msg_type":1}]}},"req_4":{"module":"GlobalComment.GlobalCommentMessageReadServer","method":"GetMessage","param":{"uin":"1152921505066834311","page_num":0,"page_size":1,"last_msg_id":"","type":0}},"req_5":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"34825437454496191","remoteplace":"txt.yqq.top","from":"yqqweb"}}}'

sign = js_compile.call("window.loader(147).default", data)

params = {
    '_': '1698845558210',
    'sign': sign,
}

response = requests.post('https://u.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers,
                         data=data)
print(response.text)