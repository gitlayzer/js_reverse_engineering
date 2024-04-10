# coding: utf-8
"""
@python version : python3.10
@file name      : QQ音乐.py
@date           : 2024/4/9 16:50
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import json
import time

import execjs
import requests

cookies = {
    'pgv_pvid': '8438644045',
    'eas_sid': 'c1Z668N3T8S6E3Q0G9K6Z9U5M7',
    'fqm_pvqid': '648bf0d3-d56a-4fb0-8749-01b0a02d6993',
    'RK': 'ODf8tN1cPA',
    'ptcz': 'b12cb2dbb2cea3efbae95de9c8b0b3b0fa1d604e6f7c0868dcc837e0860c6d04',
    '_clck': '1l6igz9|1|fhi|0',
    'qq_domain_video_guid_verify': '5eaecbe39e792ee4',
    '_qimei_uuid42': '17c12092a2b100a7d1624b6d3679af177f4e52830c',
    '_qimei_fingerprint': '55cfffdbbb0761e1aad2f0550127221c',
    '_qimei_q36': '',
    '_qimei_h38': '2db836b9d1624b6d3679af1702000002517c12',
    'ts_refer': 'www.baidu.com/link',
    'ts_uid': '7047238320',
    'fqm_sessionid': '9553ff5d-b197-4628-ad8f-7f966d7b472d',
    'pgv_info': 'ssid=s4722617538',
    'ts_last': 'y.qq.com/n/ryqq/search',
    '_qpsvr_localtk': '0.9887257199111268',
    'qm_keyst': 'W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y',
    'euin': 'oK6kowEAoK4z7ec5oKck7evkoz**',
    'wxuin': '1152921504811854453',
    'wxrefresh_token': '79_gfe0HrjiZtiG8Pea-LV6XFHBenqaST0graPjenQq-LoxNb_9owoXo6wL9ARqVheA2w9Yy2pGlDPatCNHo64KDjdN3CPyyRctf0KU4wP9ARI',
    'wxunionid': 'oqFLxslmzLyPyVmWA_Pzih8p_8WQ',
    'qm_keyst': 'W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y',
    'qqmusic_key': 'W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y',
    'tmeLoginType': '1',
    'psrf_qqrefresh_token': '',
    'psrf_qqopenid': '',
    'psrf_qqunionid': '',
    'wxopenid': 'opCFJw_oNKJI-S_kSItiQmakFb0E',
    'wxuin': '1152921504811854453',
    'psrf_qqaccess_token': '',
    'login_type': '2',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'pgv_pvid=8438644045; eas_sid=c1Z668N3T8S6E3Q0G9K6Z9U5M7; fqm_pvqid=648bf0d3-d56a-4fb0-8749-01b0a02d6993; RK=ODf8tN1cPA; ptcz=b12cb2dbb2cea3efbae95de9c8b0b3b0fa1d604e6f7c0868dcc837e0860c6d04; _clck=1l6igz9|1|fhi|0; qq_domain_video_guid_verify=5eaecbe39e792ee4; _qimei_uuid42=17c12092a2b100a7d1624b6d3679af177f4e52830c; _qimei_fingerprint=55cfffdbbb0761e1aad2f0550127221c; _qimei_q36=; _qimei_h38=2db836b9d1624b6d3679af1702000002517c12; ts_refer=www.baidu.com/link; ts_uid=7047238320; fqm_sessionid=9553ff5d-b197-4628-ad8f-7f966d7b472d; pgv_info=ssid=s4722617538; ts_last=y.qq.com/n/ryqq/search; _qpsvr_localtk=0.9887257199111268; qm_keyst=W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y; euin=oK6kowEAoK4z7ec5oKck7evkoz**; wxuin=1152921504811854453; wxrefresh_token=79_gfe0HrjiZtiG8Pea-LV6XFHBenqaST0graPjenQq-LoxNb_9owoXo6wL9ARqVheA2w9Yy2pGlDPatCNHo64KDjdN3CPyyRctf0KU4wP9ARI; wxunionid=oqFLxslmzLyPyVmWA_Pzih8p_8WQ; qm_keyst=W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y; qqmusic_key=W_X_63B0ay7fDC_aMxNr6yDb4HwUQP1abtauffCjHIwuGB20-yocCAJ3TUr9fq7d1tt9rlPPAHQGUV_qPq2Y; tmeLoginType=1; psrf_qqrefresh_token=; psrf_qqopenid=; psrf_qqunionid=; wxopenid=opCFJw_oNKJI-S_kSItiQmakFb0E; wxuin=1152921504811854453; psrf_qqaccess_token=; login_type=2',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505066834311","g_tk_new_20200303":1799252052,"g_tk":1799252052},"req_1":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"33844389614678453","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_2":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"34959302995177909","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_3":{"module":"MessageCenter.MessageCenterServer","method":"GetMessage","param":{"uin":"1152921505066834311","red_dot":[{"msg_type":1}]}},"req_4":{"module":"GlobalComment.GlobalCommentMessageReadServer","method":"GetMessage","param":{"uin":"1152921505066834311","page_num":0,"page_size":1,"last_msg_id":"","type":0}},"req_5":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"34825437454496191","remoteplace":"txt.yqq.top","from":"yqqweb"}}}'

sign = execjs.compile(open('QQ.js','r',encoding='utf-8').read()).call('getSign',data)
print(sign)
params = {
    '_': str(int(time.time()*1000)),
    'sign': sign,
}


response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)