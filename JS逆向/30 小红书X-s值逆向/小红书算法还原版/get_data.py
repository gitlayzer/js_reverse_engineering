# coding: utf-8
"""
@python version : python3.10
@file name      : get_data.py
@date           : 2024/4/8 14:05
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
    'xsecappid': 'xhs-pc-web',
    'a1': '18875c53892wgd3o71a3ws1raoh1jairz42rmepl950000266508',
    'webId': 'ca02931124837f32ccf2485d54c01bb2',
    'gid': 'yYYW2S2qdfudyYYW2S2qY4dUjJEkfqlWy0qEJ1jMyF0lxF28yV03F6888JKK28Y8qY4Dy8f2',
    'gid.sign': '1l6n/pvZdnlavsnp/0nP8GCUEhU=',
    'web_session': '030037a34b169537f1dbad0400234a4c89cc10',
    'abRequestId': 'ca02931124837f32ccf2485d54c01bb2',
    'webBuild': '4.9.0',
    'unread': '{%22ub%22:%2266072f42000000001a00c5da%22%2C%22ue%22:%22660ca319000000001a014e20%22%2C%22uc%22:20}',
    'websectiga': '3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2',
    'sec_poison_id': 'afd200e8-6a8f-44e5-ac4c-9b7d7c9202ae',
}
headers = {
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'X-t': str(int(time.time() * 1000)),
    'x-b3-traceid': 'd985eff83eb8a19b',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'X-S-Common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHFN0D1PsHVHdWMH0ijP/Wh+Ap0+/Phw/Q789cAJAqlG/+7qAbUGnRiPnkYygQC+eQUJnpIJeDMPeZIPeH9+0LIwsHVHdW9H0il+ArU+/ch+/HM+AGANsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QJLLMnS4tybkryA+ypBYi/MznySkrzfSwzF8V/DzsJLRLngYyzr83/FzzPLMgzfYyzBYxnfkdPSkoafM+zBli/Fz02bkgzgYOprFlnfMz2bSxagkOpMLF/nkwybkg/gkwzMLFnD4aySSCngkwPDLI/pz0PLMoz/z8Jp8x/nknyLET//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/SzwJrMxzg48JprInnM8+rExn/byzbDInSzp+LMCyAp82DLlnSzQ2pkLp/p8PDLFnSz8PFRopfl8PDMC/Dz3+LRozfl82f+C/DzQPSkrnfT8pr8V/F4pPSkrpfTyzrkT/Szm2SSxp/p+pbSEnpznJrMTn/zOzbrl/gkmPDMLc/Q8ySbCnpzayDMra/QypBli/F4ByLMoafkwprbEnD4+PpSCLfSOzrEx/p4tyMSxpfTyyfVAnfksyrErc/bwyfPUnSztyDEC/fkOzBVAnnkmPLETzgY+pr8V/Dzd4FMTag4wPSDMnDz8PLMCag4+pMQV/FzVySSCz/zypMDlnDzm+rEEa0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J9p/8db8aob7JeQl4eps8dbtag8BGDEPLaTyLoq7agYDq7YM47HFqgz3anTU4FSkN7+3nfPAaL+P8rDA/9LI4gzVPDbrnd+P+nprLFkALMm7nrSb4d+kpdzt/Mm7wrQM498cqBzSprzg/FSh+b8QygL9nSm7GDkl4emQ2rYEJFMm8p8M4b4Q4d8A+S8FGDSk/gkQynWUq9G9qMP7yepUpLRA8dpF+o+++npg20zn/BRt8p+g4L4Q4DESzbmFGFSkJ7+x4gcEGDlkySmDqo+QP9zSygbFP7mg+9Ll8UTNanY/qrSbnn4HJ7b8a/+/8Az0weYQygkMcS87pLS9zFGF8/8S8BHM8nTn4r+Q2rbA8fLAqAmD4pkQyepSPFziLMml4FzQyFRAPFQtqA8/8g+kqgq6qfc68LzM49kQcF8o2Db68/ml49lCJjRAL7p7qDDAJsRQPAY/JM87asRc49E6GLSwadmtqAmp/7+3pdzTanV98LzxcgPl/nPlanTNqM+P+7+hwLG7anT68/bn4e8QyFq747b7nSbM4rSQ2o8S+dpFnLS3J7+nqg4kaLpwqFzl4bpF4gqUJgb7nrS9/BzQ2opCwB8QzeQQ4fLALozpanYn2DSk/fprpd468p40G7mp/7+rq9TManYa2gzc474Cqg4manTSqM4l4oplaLbApDG9qAbQGDlQyLcRHjIj2eDjwjFl+AD7PAclw/qhNsQhP/Zjw0rIKc==',
    'Referer': 'https://www.xiaohongshu.com/',
    # 'X-s': '',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'cursor_score': '',
    'num': 30,
    'refresh_type': 1,
    'note_index': 29,
    'unread_begin_note_id': '',
    'unread_end_note_id': '',
    'unread_note_count': 0,
    'category': 'homefeed.food_v3',
    'search_key': '',
    'need_num': 10,
    'image_formats': [
        'jpg',
        'webp',
        'avif',
    ],
    'need_filter_image': False,
}
# 需要对data进行格式处理
url = "/api/sns/web/v1/homefeed"
a1 = cookies.get("a1")

x_s = execjs.compile(open('算法实现.js', 'r', encoding='utf-8').read()).call('get_x_s', url, json_data, a1)
headers['X-s'] = x_s
data = json.dumps(json_data, separators=(",", ":"))
response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', headers=headers, cookies=cookies,data=data)
print(response.json()['data']['items'])