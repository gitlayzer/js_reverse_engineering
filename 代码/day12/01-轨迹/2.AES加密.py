# @课程    : 爬虫逆向实战课
# @讲师    : 武沛齐
# @课件获取 : wupeiqi666
import base64
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

data_string = '{"openTime":1702021534202,"startTime":1702021535985,"endTime":1702021536303,"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36","uid":"0000f800254059475ae0ab8d","track":["36040;58.00;273.00;1.00","36061;112.00;277.00;55.00","36085;222.00;291.00;165.00","36108;309.00;294.00;252.00","36128;385.00;294.00;328.00","36150;405.00;294.00;348.00","36172;421.00;294.00;364.00","36192;428.00;294.00;371.00","36212;433.00;294.00;376.00","36233;443.00;294.00;386.00","36256;457.00;294.00;400.00","36276;468.00;294.00;411.00","36296;486.00;297.00;429.00"],"acc":[],"ori":[],"deviceMotion":[{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true},{"isTrusted":true}]}'
# key = "227V2xYeHTARSh1R".encode('utf-8')
key_string = "32323756327859654854415253683152"
key = binascii.a2b_hex(key_string)


aes = AES.new(
    key=key,
    mode=AES.MODE_ECB
)
raw = pad(data_string.encode('utf-8'), 16)
aes_bytes = aes.encrypt(raw)
res = base64.b64encode(aes_bytes)
print(res)

# "/rbk3gF/w9E6nxeN9/KAwkfV/Suaadocu+lITcBeF8Otqk1I7U5YdIehRxzb3zQmP3nuWBUTC3eYj2iITgNXxqUEwqHFnIehVq4aj2POYtbbwIYdS4ceo1kLfu+9Hxv4Pf1bQK7GBdkHOn+pynXZ5rf/Cry06pPfR/Hf7BrFSk1rvLNqcTBvq6730+O1VcEkBJTDTx/lnSA+jwK9ypQ44HRjonU347dLl4qbCximrSMU4Ffa8UWz5/7Za6IUpI8bGJBsICcW13u/6VrdJ1k9i4R0Prk8WdJuRpPDmIzzHtIGj0jWVcoGykitY334e/I3HBU0J/9zF4IVyilOvRoCHlNCX33K/W7o8ZfhTuyEHeSmfUDXII+y60so3sgjyL6Jx2mPbqAUf4i3BN0Nf8+Ehmop4nOd/4umofKpm8l3CNKBmsyKr+Lqd4PM0ePZnNsy8z6K4fZYN/Z/3cK8fD6Ud3uaIIBmoAkNOBwOYs/a2Qp4U4qa57YtADX/SpDbBGlX+P2knhf7c4WU7qMJW6UzFA/1woeCPGNBbxwxhh/7fC0E/tmOnvNZWeohdzc86US7Ic0MrdHeX9bsQ3dGBPy86XZ6j2fJSYNwxfB3m4ExpeEDtg09manx7bkh8qXv4LpLMDfnzhAz/wJ9ikXYq93ImkAlu5PWFWsKycWz2scjfhg48P+aP/OHkbKV2th/b97Np3iHNye/HQA4zTadhYs0EIKu5YTCp5l1xLDKxuz3P/xFW6BtATFuF5MpH0mljqahfBpV9puaOaCyDP3zIgGTIWqniLuY3HqA3yLZ6IUCorv94ueBMYHq1MwAIzL32OjfviDgo+7B9qh9zVQukaR2gwSmia+CRDJ2uwyZUETpm3NOzhR356QqA+IvQ2aHc7zKnKk3M7fJBrZNDi6sELSRVOVsdO+7uxrqQu7c0h9/NxNeNiBRN5LaB5R+ocEji3KeR6IZbrOAtcIS9RNkOHu0P/G2yNNJc372MPQtfjnzRwKFf8VcRH/zsFhQuA/KZSDqYQBU/4L4Drj8BGNSF38kUPU2GkEFTTigl5RrL1qEBX7xXK+6PIjrKcYC0HlDR0UvmjMMi9JKMMJAPR4FHBDh6hsZmjmMayZVBwgTUQ9DubuLOzB9+B4/Dn6dYM1rxJNlZMzHuAkhnb1Qm3ewUWA3+S6m49NpM1GTYTjP4G9I5s2+BkingUHSxSD5qBIHRUwamypxs71L3mUXtScON+PWa9K+9Ruib9Jjr6ZkXN5jv9mTAQt7vEKXxQBdivxADUY9Ts4Ud+ekKgPiL0Nmh3O8ypypNzO3yQa2TQ4urBC0kVTlbHTvu7sa6kLu3NIffzcTXjYgUTeS2geUfqHBI4tynkeiGW6zgLXCEvUTZDh7tD/xtsjTSXN+9jD0LX4580cChX/FXER/87BYULgPymUg6mEAVP+C+A64/ARjUhd/JFD1NhpBBU04oJeUay9ahAV+8VyvujyI6ynGAtB5Q0dFL5ozDIvSSjDCQD0eBRwQ4eobGZo5jGsmVQcIE1EPQ7m7izswffgePw5+nWDNa8STZWTMx7gJIZ29UJt3sFFgN/kupuPTaTNRk2E4z+BvSObNvgZIp4FB0sUg+agSB0VMGpsqcbO9S95lF7UnDjfj1mvSvvUbom/SY6+mZFzeY7/ZkwELe7xCl8UAXYr8QA1GPU7OFHfnpCoD4i9DZodzvMqcqTczt8kGtk0OLqwQtJFU5Wx077u7GupC7tzSH383E142IFE3ktoHlH6hwSOLcp5Hohlus4C1whL1E2Q4e7Q/8bbI00lzfvYw9C1+OfNHAoV/xVxEf/OwWFC4D8plIOphAFT/gvgOuPwEY1IXfyRQ9TYaQQVNOKCXlGsvWoQFfvFcr7o8iOspxgLQeUNHRS+aMwyL0kowwkA9HgUcEOHqYHfDji5duSuitXuWLO57/A=="
# '/rbk3gF/w9E6nxeN9/KAwkfV/Suaadocu+lITcBeF8Otqk1I7U5YdIehRxzb3zQmP3nuWBUTC3eYj2iITgNXxqUEwqHFnIehVq4aj2POYtbbwIYdS4ceo1kLfu+9Hxv4Pf1bQK7GBdkHOn+pynXZ5rf/Cry06pPfR/Hf7BrFSk1rvLNqcTBvq6730+O1VcEkBJTDTx/lnSA+jwK9ypQ44HRjonU347dLl4qbCximrSMU4Ffa8UWz5/7Za6IUpI8bGJBsICcW13u/6VrdJ1k9i4R0Prk8WdJuRpPDmIzzHtIGj0jWVcoGykitY334e/I3HBU0J/9zF4IVyilOvRoCHlNCX33K/W7o8ZfhTuyEHeSmfUDXII+y60so3sgjyL6Jx2mPbqAUf4i3BN0Nf8+Ehmop4nOd/4umofKpm8l3CNKBmsyKr+Lqd4PM0ePZnNsy8z6K4fZYN/Z/3cK8fD6Ud3uaIIBmoAkNOBwOYs/a2Qp4U4qa57YtADX/SpDbBGlX+P2knhf7c4WU7qMJW6UzFA/1woeCPGNBbxwxhh/7fC0E/tmOnvNZWeohdzc86US7Ic0MrdHeX9bsQ3dGBPy86XZ6j2fJSYNwxfB3m4ExpeEDtg09manx7bkh8qXv4LpLMDfnzhAz/wJ9ikXYq93ImkAlu5PWFWsKycWz2scjfhg48P+aP/OHkbKV2th/b97Np3iHNye/HQA4zTadhYs0EIKu5YTCp5l1xLDKxuz3P/xFW6BtATFuF5MpH0mljqahfBpV9puaOaCyDP3zIgGTIWqniLuY3HqA3yLZ6IUCorv94ueBMYHq1MwAIzL32OjfviDgo+7B9qh9zVQukaR2gwSmia+CRDJ2uwyZUETpm3NOzhR356QqA+IvQ2aHc7zKnKk3M7fJBrZNDi6sELSRVOVsdO+7uxrqQu7c0h9/NxNeNiBRN5LaB5R+ocEji3KeR6IZbrOAtcIS9RNkOHu0P/G2yNNJc372MPQtfjnzRwKFf8VcRH/zsFhQuA/KZSDqYQBU/4L4Drj8BGNSF38kUPU2GkEFTTigl5RrL1qEBX7xXK+6PIjrKcYC0HlDR0UvmjMMi9JKMMJAPR4FHBDh6hsZmjmMayZVBwgTUQ9DubuLOzB9+B4/Dn6dYM1rxJNlZMzHuAkhnb1Qm3ewUWA3+S6m49NpM1GTYTjP4G9I5s2+BkingUHSxSD5qBIHRUwamypxs71L3mUXtScON+PWa9K+9Ruib9Jjr6ZkXN5jv9mTAQt7vEKXxQBdivxADUY9Ts4Ud+ekKgPiL0Nmh3O8ypypNzO3yQa2TQ4urBC0kVTlbHTvu7sa6kLu3NIffzcTXjYgUTeS2geUfqHBI4tynkeiGW6zgLXCEvUTZDh7tD/xtsjTSXN+9jD0LX4580cChX/FXER/87BYULgPymUg6mEAVP+C+A64/ARjUhd/JFD1NhpBBU04oJeUay9ahAV+8VyvujyI6ynGAtB5Q0dFL5ozDIvSSjDCQD0eBRwQ4eobGZo5jGsmVQcIE1EPQ7m7izswffgePw5+nWDNa8STZWTMx7gJIZ29UJt3sFFgN/kupuPTaTNRk2E4z+BvSObNvgZIp4FB0sUg+agSB0VMGpsqcbO9S95lF7UnDjfj1mvSvvUbom/SY6+mZFzeY7/ZkwELe7xCl8UAXYr8QA1GPU7OFHfnpCoD4i9DZodzvMqcqTczt8kGtk0OLqwQtJFU5Wx077u7GupC7tzSH383E142IFE3ktoHlH6hwSOLcp5Hohlus4C1whL1E2Q4e7Q/8bbI00lzfvYw9C1+OfNHAoV/xVxEf/OwWFC4D8plIOphAFT/gvgOuPwEY1IXfyRQ9TYaQQVNOKCXlGsvWoQFfvFcr7o8iOspxgLQeUNHRS+aMwyL0kowwkA9HgUcEOHqYHfDji5duSuitXuWLO57/A=='