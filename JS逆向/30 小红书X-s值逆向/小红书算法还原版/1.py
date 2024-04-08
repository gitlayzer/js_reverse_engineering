import requests
import json
import execjs

cookies = {
    'abRequestId': '3c7aeb7d-f7be-54fb-9df5-f1ec0a4073f1',
    'webBuild': '4.5.3',
    'a1': '18e3653ac5b70xvg4bhb6vn01mtd6puy05edxohpy30000145916',
    'webId': 'ff090713e2f99ec46a3c0350dbf2a634',
    'web_session': '030037a2c268216a2f74197a89224ab1124606',
    'gid': 'yYdqK2qDy888yYdqK2q0S2lx2DW8Chk4DxDKdUvhI8y69fq8fKU7vC888y42jyK8KYf2KqJj',
    'unread': '{%22ub%22:%2265d57d04000000000b018c92%22%2C%22ue%22:%2265e54a8100000000040015d0%22%2C%22uc%22:25}',
    'xsecappid': 'xhs-pc-web',
    'websectiga': '634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a',
    'sec_poison_id': 'e63cf3cb-eb1c-4d7d-babb-4472ba9ae624',
}

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'abRequestId=3c7aeb7d-f7be-54fb-9df5-f1ec0a4073f1; webBuild=4.5.3; a1=18e3653ac5b70xvg4bhb6vn01mtd6puy05edxohpy30000145916; webId=ff090713e2f99ec46a3c0350dbf2a634; web_session=030037a2c268216a2f74197a89224ab1124606; gid=yYdqK2qDy888yYdqK2q0S2lx2DW8Chk4DxDKdUvhI8y69fq8fKU7vC888y42jyK8KYf2KqJj; unread={%22ub%22:%2265d57d04000000000b018c92%22%2C%22ue%22:%2265e54a8100000000040015d0%22%2C%22uc%22:25}; xsecappid=xhs-pc-web; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=e63cf3cb-eb1c-4d7d-babb-4472ba9ae624',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-b3-traceid': '5c8da89af2e40ac1',
    'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImRlYzU3MDgwMjhjMWY2Y2M0NTMzZmIyNzA3YWRhNTc0ZjU2YTQ1ZWYxMDYzMWE0MWIyZDEzY2Q5NTMzODBkZjEzYTI0ZWQxMDQ3ZWI2YzU4Y2M2M2JmNjRkMmYwN2M1MWM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNWE2ODk0YzQ2M2M1MjE0YTdjMzUyYjkxNzQwNzZhYTM4NzFmNGJjN2M5MDQ5YzQyYTk2MWY0N2Q2ODE3OGVkYmM2NmI5YmFhZmYyMGJhNjYzNmRjMjc2N2UyNzE1ZjExNTM3NmNlM2M3NTgyYWUzOTdkMGNlOTcxNDY4YzkyYzg2OWM5OTk4NjM5ZjRlNWE4NjMzOWZmZGM2MmI5MWRhNmNmNmY0ODRlODVhYWRjZWUwNzI2MDI5MTAyMGM4Y2FiYSJ9',
    'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0c1+ahAHjIj2eLjwjHlwBLA+0LAGnPMG0qI2o8d+BQiG089J0ZlJgzD+dmM2/ZM8nzhJ9YI2/PIPeZIP/cMw/r9HjIj2eGjw0r7P/ZAP/ql+/qIPeWVHdW7H0ijnbSgg9pEadkYp9zMp/+y4LSxJ9Swprpk/r+t2fbg8opnaBl7nS+Q+DS187YQyg4knpYs4M+gLnSOyLiFGLY+4B+o/gzDPS8kanS7ynPUJBEjJbkVG9EwqBHU+BSOyLShanS7yn+oz0pjzASinD+Q+DSTLfl82SLA/Lzd4FMxyBk+pMDUn/Q+PrEL/gkyJLSE/dkmPMSgLfYwpBPInfkpPSSLL/bypMSh/Lz82DMgz/m+pFSEnDzb2SDUL/pwprMC/FzsyMkxzgk8prDInS4z2rMrL/+ypFDUngkp+bDU//Q+PDkT/fkayFMTng4wPDFl/p4++pkL/fSyJpQi/p4yybSLzfl8yfT7nDz0PbSgzgk+pFDl/D4+PFMT/fT+zMrA/D4ByrMCzfSwpbQx/dktySkozfkwzBqMnnkVyMSLyBkypb8V/DziJLEozfM8yflin/QyyDFUpfY+ySkTnSzsyLMxn/Q8pbkk/D4wyDFU/fSwpFLU/Fz3PbSCL/Q+PDFl/nkbPbSL8Bk+2SpEnnk32rECLg4w2Skinpz++rECzfMwzFkx/0Q++LMrL/p82SbEnpz3PDMgn/mwPSrU/FzbPFRopfT8JLFU/fMQ+pSTzfYyJpSE/L4tyrExngkwJpQx/nk0PDhUpgSw2DLlnfkb2rEL//+wJLEV//Q+PFEL87S8pMpC/MzDyFMo/flOpB+h/Dz8+bSCy7S82fqU/M4++LRLyAzwyDFMnfkaJrEgz/zwyDMC/M4yJpko//Q+JLDM/p4ayrET/fMwJpDI/FzaJrRrpfY8pMQxnS4p4FECa/Q+zrDM/pzm2LMo//z8PD8knp+twaHVHdWhH0ija/PhqDYD87+xJ7mdag8Sq9zn494QcUT6aLpPJLQy+nLApd4G/B4BprShLA+jqg4bqD8S8gYDPBp3Jf+m2DMBnnEl4BYQyrkSL9E+zrTM4bQQPFTAnnRUpFYc4r4UGSGILeSg8DSkN9pgGA8SngbF2pbmqbmQPA4Sy9MaPpbPtApQy/8A8BE68p+fqpSHqg4VPdbF+LQfqLkQ4D8j/DlztMkc4A4Q2BzA2op7q0zl4BTQy7Q7anD6q9TyGA+QcFlDa/+O8/mM4BIUcLzyqFIM8Lz/ad+/Lo4GaLp9q9Sn4rkOLoqhcdp78SmI8BpLzb4OagWFpDSk4/8yLo4jadbFPrShaoS6/LbSpdpFpFS94dP9qgz1anD3aFSb2fbSJA8APeSoPnLI+g+84gzFqfQ68/mBzS4IwLTSPbSlLLShN9prLo4TanSt8n8l4rbCnS8n/7+M4FDA8BpL4gzmNMS98/G7qeQQybSCaLpLPDY6qnkQPM+EwrS88FSbyrSs4g4/aL+ipjV6a9pDqepSP7bF4LDA+d+xG/4APB8H+rS3+npkqfFMa7b78DSka7+LJ78SPp+NqA+c4MmT8LRS8ob7pDDA+rlYp/8SL7b7y7kd8o+gpdc3a/+3aFShJnzAqgzTqSmFcfE1a/zTcLbAzB8d8gYn49QQyrkS8BEOq7YCn0FjNsQhwaHCN/DI+eDF+AqM+sIj2erIH0iU+gF=',
    'x-t': '1710317157008',
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

# 获取x-s
x_s = execjs.compile(open("01 算法测试.js",encoding='utf-8').read()).call("get_x_s", "/api/sns/web/v1/homefeed", json_data,
                                                         cookies.get("a1"))
print(x_s)

headers["x-s"] = x_s
data = json.dumps(json_data, separators=(",", ":"))

response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/homefeed', cookies=cookies, headers=headers,
                         data=data)
print(response.text)
