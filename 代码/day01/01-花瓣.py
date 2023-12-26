import requests
import json

res = requests.get(
    url="https://api.huaban.com/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations"
)

# print(res.text)
data_dict = json.loads(res.text)
pin_list = data_dict["pins"]
for item in pin_list:
    print(item['user']['username'], item['raw_text'])

