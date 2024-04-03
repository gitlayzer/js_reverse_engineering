const CryptoJS = require('crypto-js');


d = function (data) {
    return CryptoJS.MD5(data).toString()
}
l = {
    key: CryptoJS.enc.Utf8.parse("fX@VyCQVvpdj8RCa"),
    iv: CryptoJS.enc.Utf8.parse(function (t) {
        for (var e = "", i = 0; i < t.length - 1; i += 2) {
            var n = parseInt(t[i] + "" + t[i + 1], 16);
            e += String.fromCharCode(n)
        }
        return e
    }("00000000000000000000000000000000"))
}
v = function (data) {
    return function (data) {
        return CryptoJS.AES.encrypt(data, l.key, {
            iv: l.iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }(data)
}
f = function (t) {
    var e = "";
    return Object.keys(t).sort().forEach((function (n) {
            e += n + ("object" === typeof (t[n]) ? JSON.stringify(t[n], (function (t, e) {
                    return "number" == typeof e && (e = String(e)),
                        e
                }
            )).replace(/\//g, "\\/") : t[n])
        }
    )),
        e
}

// 获取加密函数需要的参数 U M c
var get_5_random = function () {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 5;
    return Math.random().toString(36).substring(3, 3 + e)
}
var D = parseInt((new Date).getTime() / 1e3)


var M = {
    "username": "18761661218",
    "password": "ddsafadf",
    "code": "yvsfv",
    "hdn_refer": "https://zt.epwk.com/"
}

// 生成sign的函数
get_sign = function (t) {
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "a75846eb4ac490420ac63db46d2a03bf"
        , n = e + f(data) + f(t) + e;
    return n = d(n),
        n = v(n)
}


function getHeaders(M) {
    var c = 'a75846eb4ac490420ac63db46d2a03bf'
    var U = {
        "App-Ver": "",
        "Os-Ver": "",
        "Device-Ver": "",
        "Imei": "",
        "Access-Token": "",
        "Timestemp": D,
        "NonceStr": `${D}${get_5_random()}`,
        "App-Id": "4ac490420ac63db4",
        "Device-Os": "web"
    }
    U['Signature'] = get_sign(U, M, c)
    U['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    U['X-Request-Id']='29a06929c30fccd8a0b0a9923d8b886f'
    U['Timestemp'] = U['Timestemp'].toString()

    return U
}

// 获取登录的headers
console.log(getHeaders(M))
// 获取验证码的headers
console.log(getHeaders({}))