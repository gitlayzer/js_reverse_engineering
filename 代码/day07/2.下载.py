import requests

res = requests.get(url="https://zz123.com/xplay/?act=songplay&id=vakas", allow_redirects=False)
mp3_url = res.headers['Location']

res = requests.get(url=mp3_url)

with open("晴天.mp3", mode='wb') as f:
    f.write(res.content)
