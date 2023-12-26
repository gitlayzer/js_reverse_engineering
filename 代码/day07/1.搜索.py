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
    print(item)
