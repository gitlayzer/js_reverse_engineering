const CryptoJs = require('crypto-js')
require('./env')
require('./mod')
let params = {
    async: true,
    body: "first=true&cl=false&fromSearch=true&labelWords=&suginput=&city=&kd=Java",
    headers: {
        accept: 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-anit-forge-token': 'ca7a932b-0fa2-434a-bd51-7bbef61d207e',
        'x-anit-forge-code': '34ad7690-8034-42b8-b575-02fd422486fa'
    },
    method: "POST",
    password: undefined,
    url: "https://www.lagou.com/jobs/v2/positionAjax.json",
    user: undefined,
    withCredentials: true,
}
// 获取X-S-header
let T = window.loader('517')

function get_X_S_header() {
    return T.A2(params)
}

function getEncryptData(s) {
    let A = window.loader('375')
    //let s ='first=true&needAddtionalResult=false&city=%E5%85%A8%E5%9B%BD&pn=3&cl=false&fromSearch=true&kd=python'
    return T.q6(JSON.stringify(A.$Z("?".concat(s))))
}

// let ee = ''
// ee = JSON.stringify(ee.replace(/[\n]/g, ''))
// function Decrypt(encrypt_data) {
//     return JSON.stringify(T.ow(encrypt_data))
// }

decryptResData = function (t) {
    let kt = CryptoJs.enc.Utf8.parse('=QW/zcdxH=JUMXJkYCiAJxNXr4XLDnWq');
    t = CryptoJs.AES.decrypt(t, kt, {
        iv: {
            "words": [
                1664431416,
                1198600281,
                1363882577,
                1433161059
            ],
            "sigBytes": 16
        },
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    }).toString(CryptoJs.enc.Utf8);
    try {
        t = JSON.parse(t)
    } catch (t) {
    }
    return t
}

