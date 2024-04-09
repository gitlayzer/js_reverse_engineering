# coding: utf-8
"""
@python version : python3.10
@file name      : 抖音.py
@date           : 2024/4/9 13:06
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
import execjs
from urllib.parse import urlencode, urlparse

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'bd_ticket_guard_client_web_domain=2; ttwid=1%7Cl57kJluohIpXFkzxDWasIXGEvTgAg4_S1IoBN5byXDQ%7C1703727100%7C50e3b16b3f119c7ad8a2c12c4b7b1c5979ba60780922ee8af46f9f9881908382; n_mh=NNt04G4vM5zW2aP23uqPZQsdsGWAsBG1dZcb3n1GFb0; toutiao_sso_user=4e0eeb25bbc1883a9c0b48738d17553a; toutiao_sso_user_ss=4e0eeb25bbc1883a9c0b48738d17553a; passport_csrf_token=d7a623fc97fd3bdab6644e6245f5ec43; passport_csrf_token_default=d7a623fc97fd3bdab6644e6245f5ec43; store-region=cn-sh; store-region-src=uid; douyin.com; device_web_cpu_core=6; device_web_memory_size=8; architecture=amd64; dy_swidth=2560; dy_sheight=1440; csrf_session_id=c19393aba5e45e8dd4f3eac81fca6999; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA5VWuv6nIRmrO6E6E4OacKYv8ZE-7KZJHYizB3yjY3Fo%2F1712678400000%2F0%2F1712631611318%2F0%22; strategyABtestKey=%221712631611.859%22; xg_device_score=7.195435614229755; publish_badge_show_info=%220%2C0%2C0%2C1712631616021%22; LOGIN_STATUS=0; sso_uid_tt=9f42530f5f111c3c7b451af9d56be45b; sso_uid_tt_ss=9f42530f5f111c3c7b451af9d56be45b; sid_ucp_sso_v1=1.0.0-KGM2OTBhMWNjNjE4ZTM2N2E5YWYxYmI0ZWExMDhkNzlmOTFjYTM2ZmUKCRDM3tKwBhjvMRoCbHEiIDRlMGVlYjI1YmJjMTg4M2E5YzBiNDg3MzhkMTc1NTNh; ssid_ucp_sso_v1=1.0.0-KGM2OTBhMWNjNjE4ZTM2N2E5YWYxYmI0ZWExMDhkNzlmOTFjYTM2ZmUKCRDM3tKwBhjvMRoCbHEiIDRlMGVlYjI1YmJjMTg4M2E5YzBiNDg3MzhkMTc1NTNh; odin_tt=ba865be686d506ddf2ed0935a9f999ccdb873b0f7ba444449f54bdcc72cc122d; sid_guard=b4a023824af39bee361ac7da8ba35b4d%7C1712631628%7C21600%7CTue%2C+09-Apr-2024+09%3A00%3A28+GMT; uid_tt=6c747f263cc2991dd52329ee1ddbdeac; uid_tt_ss=6c747f263cc2991dd52329ee1ddbdeac; sid_tt=b4a023824af39bee361ac7da8ba35b4d; sessionid=b4a023824af39bee361ac7da8ba35b4d; sessionid_ss=b4a023824af39bee361ac7da8ba35b4d; sid_ucp_v1=1.0.0-KGMxNDZkNjVjNzJjZDU2MDRiMGRmZGRiZjIxZjEzYzRhNzVmMDFkMjcKCBDM3tKwBhgNGgJobCIgYjRhMDIzODI0YWYzOWJlZTM2MWFjN2RhOGJhMzViNGQ; ssid_ucp_v1=1.0.0-KGMxNDZkNjVjNzJjZDU2MDRiMGRmZGRiZjIxZjEzYzRhNzVmMDFkMjcKCBDM3tKwBhgNGgJobCIgYjRhMDIzODI0YWYzOWJlZTM2MWFjN2RhOGJhMzViNGQ; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.529%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSld5ZHJkNHVPQnAxWHlhUHF2eHpKNFRtYmlsQ2UvYXY4MEx3eTZKcGNFUzBINldaK2drYVNaMEpEUTErdDI2c1l5RDZ4ek1wV0lvVWJhU0o1TjIrd3M9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%222%2F20240409%2F0%22; GlobalGuideTimes=%221712631736%7C3%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=06614b7000015b2ec80f0; __ac_signature=_02B4Z6wo00f01REFKJQAAIDCLKwyCEb.CO0RJSwAACJYujjmjAs2OexMk2owvWZG6phKfiSiK-oURBjQybnUb5Pvbvfe.6aTZnGQ8dymW0VEIng83WGAzV25Z34cWp72tzQAw5ZmrplR8s4629; tt_scid=m3ozyS.oXO4DsztIr.mpauyBQK8JNDZPjqhi7JQrUA07CBdB.3hGtlIRp-sm3jHzdf9c; msToken=AuZTDGk1V177D9hzdMob4CwivkVu6nvzNs6p9X3pFlXGxxrQUBeAzco-uao5m_-4FRDWSOmBDGtYsr10BKJ_kr9dxLGOgxFqDPk6yPAtv_0MDBGXGFx5rvLqp5-vq6c=; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A6%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; IsDouyinActive=false; msToken=F04nqsC5Auv934MJiAqgrx7JS9XO5G229udpmRRq_8pDxGx_t_YQoNsUy6qd5HPrdd8m4REg5hMz8OzAGPpyMCJ-Luv3kIkljAA8YE3rwOhOZQznVqqtB6BGk_FgmB0=',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAA5VWuv6nIRmrO6E6E4OacKYv8ZE-7KZJHYizB3yjY3Fo',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
params = "device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA5VWuv6nIRmrO6E6E4OacKYv8ZE-7KZJHYizB3yjY3Fo&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7317452119215326720&msToken=F04nqsC5Auv934MJiAqgrx7JS9XO5G229udpmRRq_8pDxGx_t_YQoNsUy6qd5HPrdd8m4REg5hMz8OzAGPpyMCJ-Luv3kIkljAA8YE3rwOhOZQznVqqtB6BGk_FgmB0%3D&a_bogus=xymqQDuDDkDBhf6V56VLfY3q6UP3Ym2%2F0trEMD2fxV39e639HMYq9exyXc4v05WjLT%2FAIeyjy4haT3nprQVjMZw39WXO%2F2CgQ600tMMh-VSts1feejuQnU4NmktWCFn25JZ4EKi8o7%2FaSYEgl9Be-wo6bfebYrtswnuYt9%2FbpD%3D%3D"

# print(url_code_params)
X_Bogus = execjs.compile(open('xb.js', 'r', encoding='utf-8').read()).call('window.yang', params)
url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?' +params +'&X-Bogus='+X_Bogus
print(url)
response = requests.get(url=url, headers=headers)
print(response.text)
