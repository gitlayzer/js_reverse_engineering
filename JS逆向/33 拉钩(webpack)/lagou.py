import requests
import execjs

cookies = {
    'user_trace_token': '20231226161655-4b89bca4-9893-46e1-9666-708cdd27d173',
    '_ga': 'GA1.2.745053790.1703578616',
    'LGUID': '20231226161655-ba5e7eda-e4b8-4570-8c47-bf21581e5b27',
    '_gid': 'GA1.2.1538962494.1712650741',
    'sajssdk_2015_cross_new_user': '1',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1712713432',
    'LGRID': '20240410094519-dfc0fe8d-04a2-4a4c-ac30-9939c0f85862',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1712713514',
    '_ga_DDLTLJDLHH': 'GS1.2.1712713433.1.1.1712713514.60.0.0',
    'gate_login_token': 'v1####0a3f48fb36dba646c8d59b95dc58581e01ef42a3c6850ff2',
    '_putrc': '837257FB671CEA1A',
    'JSESSIONID': 'ABAABJAACCIACAHA23319859DE840F5EBD01B4EBE4DF7E8',
    'login': 'true',
    'unick': '%E6%9D%A8%E5%AD%90%E6%B4%8B',
    'showExpriedIndex': '1',
    'showExpriedCompanyHome': '1',
    'showExpriedMyPublish': '1',
    'hasDeliver': '60',
    'privacyPolicyPopup': 'false',
    'WEBTJ-ID': '20240410094911-18ec5b1dbd96a8-0b7fb1cb294ccc-26001a51-3686400-18ec5b1dbda2045',
    'sensorsdata2015session': '%7B%7D',
    '__lg_stoken__': 'b4940ed2bc342891100ad935eebe120700e2209af95c6efe7ed38bebcb180afdc7d0fb9d0c80783e1a45d8b5b0e43cbfa72ec935ec922fc369e3eeedaee97455b2b859270050',
    'X_MIDDLE_TOKEN': 'cb3fe9d55d1c21135afcf70b6ab02cbf',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218ec5acfb465c8-023c5ad19c12a2-26001a51-3686400-18ec5acfb474d3%22%2C%22%24device_id%22%3A%2218ec5acfb465c8-023c5ad19c12a2-26001a51-3686400-18ec5acfb474d3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22123.0.0.0%22%7D%7D',
    'X_HTTP_TOKEN': '5ecaa4643c5778d414202721716b85f3c82642b273',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/wn/jobs?pn=2&cl=false&fromSearch=true&kd=python',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-K-HEADER': 'anz95XWYBKTf52tJmNJWyIOZuwo5cMNTPaNG8Q11+fxocB2THunvFsewvggfS7d5',
    # 'X-S-HEADER': 'tAyj4O3gdAx6egXz5XuF6BG2XtYRAuWj9Ctr3xWRhcHSNANTntZzyb6zh9RLnq/AGMGj4JRfqFs3bxpykQVZ8XRQ1UI0awvAMQzKBGW8+eQMRUpacuEojSC9tgpPd9Wz8Tot+NrSa+HMKB3hSb/xgA==',
    'X-SS-REQ-HEADER': '{"secret":"anz95XWYBKTf52tJmNJWyIOZuwo5cMNTPaNG8Q11+fxocB2THunvFsewvggfS7d5"}',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-9786654ed4600fb8a772b55eb9b7774b-04280d36173afbea-01',
    'x-anit-forge-code': 'bd02cfb3-222c-4b71-bf22-5344d0af7104',
    'x-anit-forge-token': 'f90b5994-d649-45b6-a024-c3811d58c80e',
}
JS = execjs.compile(open('lago.js', 'r', encoding='utf-8').read())
x_s_header = JS.call('get_X_S_header')
keyword = 'python'
city = '全国'
query_string = f'first=true&needAddtionalResult=false&city={city}&pn=3&cl=false&fromSearch=true&kd={keyword}'
encrypt_data = JS.call('getEncryptData')
headers['X-S-HEADER'] = x_s_header
data = {
    'data': encrypt_data,
}
# print(x_s_header)
# print(encrypt_data)
response = requests.post('https://www.lagou.com/jobs/v2/positionAjax.json', cookies=cookies, headers=headers, data=data)
encrypt_res_data = response.json()['data']
plain_data = JS.call('decryptResData', encrypt_res_data)
print(plain_data)
