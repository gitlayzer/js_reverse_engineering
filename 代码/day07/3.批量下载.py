import requests

res = requests.post(
    url="https://zz123.com/ajax/",
    data={
        "act": "search",
        "key": "周杰伦",
        "lang": "",
        "page": "1",
    }
)

res_dict = res.json()
data_list = res_dict['data']
for item in data_list:
    mp3_id = item['id']
    mp3_name = item['mname']

    res = requests.get(url=f"https://zz123.com/xplay/?act=songplay&id={mp3_id}", allow_redirects=False)
    mp3_url = res.headers['Location']

    res = requests.get(url=mp3_url)

    with open(f"{mp3_name}.mp3", mode='wb') as f:
        f.write(res.content)

    break
