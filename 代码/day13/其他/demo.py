# @课程    : 爬虫逆向实战课
# @讲师    : 武沛齐
# @课件获取 : wupeiqi666
import binascii
import hmac
from hashlib import sha1

key_string = "68386673614b337771652b696f4d7673"
key = binascii.a2b_hex(key_string)
data = '40450e94c5aa344460ef3363f0cabffe7fOOyzy-rotp_WORtvsxe["slideToken"]'

hmac_code = hmac.new(key, data.encode("utf-8"), sha1)
res = hmac_code.hexdigest()
print(res)

