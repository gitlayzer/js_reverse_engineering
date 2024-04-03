# coding: utf-8
# https://www.qimai.cn/ 逆向请求参数

import requests
import execjs

cookies = {
    'PHPSESSID': 'ttokkljdchjb0ji2t26d1p370p',
    'qm_check': 'A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdASAFKBQcCCXtzdRFFIg4aHRoOBnMDARlGR2dQOVdICAolAGgCHBl0B3xUV05KVFsZXVJRWxsKFghJVktYVElWBRVP',
    'gr_user_id': '135dc951-de44-4610-b824-acc3e61f574c',
    'ada35577182650f1_gr_session_id': '2b49861f-84c8-48b0-b5ac-224026fead26',
    'ada35577182650f1_gr_session_id_sent_vst': '2b49861f-84c8-48b0-b5ac-224026fead26',
    'tgw_l7_route': '29ef178f2e0a875a4327cbfe5fbcff7e',
    'synct': '1712155724.373',
    'syncd': '-3731',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'PHPSESSID=ttokkljdchjb0ji2t26d1p370p; qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdASAFKBQcCCXtzdRFFIg4aHRoOBnMDARlGR2dQOVdICAolAGgCHBl0B3xUV05KVFsZXVJRWxsKFghJVktYVElWBRVP; gr_user_id=135dc951-de44-4610-b824-acc3e61f574c; ada35577182650f1_gr_session_id=2b49861f-84c8-48b0-b5ac-224026fead26; ada35577182650f1_gr_session_id_sent_vst=2b49861f-84c8-48b0-b5ac-224026fead26; tgw_l7_route=29ef178f2e0a875a4327cbfe5fbcff7e; synct=1712155724.373; syncd=-3731',
    'origin': 'https://www.qimai.cn',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
url = 'https://api.qimai.cn/indexV2/getIndexRank'
params = {
    # 'analysis': 'eyErVShbVhNbVVIbMlMWUQASLgYcHAJnUFkIJEIMBlxVVl5NTEsDAXdAVw==',
    'setting': '0',
    'genre': '36',
}
analysis = execjs.compile(open('优化版.js','r',encoding='utf-8').read()).call('get_analysis',url,params)
params['analysis'] = analysis

response = requests.get(url=url,params=params, cookies=cookies, headers=headers)
print(response.content.decode('unicode_escape')) #解决 \u70ed\u95e8\u5730\u533a 转中文