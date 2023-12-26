import requests
import ddddocr

res = requests.post(url="https://api.ruanwen.la/api/auth/captcha/generate")
res_dict = res.json()

captcha_token = res_dict['data']['captcha_token']
captcha_src = res_dict['data']['src']

res = requests.get(url=captcha_src)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)

# 登录认证
res = requests.post(
    url="https://api.ruanwen.la/api/auth/authenticate",
    json={
        "mobile": "18766655555",
        "device": "pc",
        "password": "qwe123",
        "captcha_token": captcha_token,
        "captcha": code,
        "identity": "advertiser"
    }
)
print(res.json())
# {'success': False, 'message': '账号不存在', 'status': 200}
# {'success': True, 'message': '验证成功', 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5ydWFud2VuLmxhL2FwaS9hdXRoL2F1dGhlbnRpY2F0ZSIsImlhdCI6MTcwMTY1MzI2NywiZXhwIjoxNzA1MjUzMjY3LCJuYmYiOjE3MDE2NTMyNjcsImp0aSI6IjQ3bk05ejZyQ0JLV28wOEQiLCJzdWIiOjUzMzEyNTgsInBydiI6IjQxZGY4ODM0ZjFiOThmNzBlZmE2MGFhZWRlZjQyMzQxMzcwMDY5MGMifQ.XxFYMEot-DfjTUcuVuoCjcBqu3djvzJiTeJERaR95co'}, 'status': 200}
