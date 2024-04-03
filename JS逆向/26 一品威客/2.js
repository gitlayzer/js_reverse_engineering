const CryptoJS = require('crypto-js');


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
d = function (data) {
    return CryptoJS.MD5(data).toString()
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
//Object(h.e) 构建NonceStr 后面的随机字符串
get_random_str = function () {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 5;
    return Math.random().toString(36).substring(3, 3 + e)
}
var D = parseInt((new Date).getTime() / 1e3)
var U = {
    "App-Ver": "",
    "Os-Ver": "",
    "Device-Ver": "",
    Imei: "",
    "Access-Token": "",
    Timestemp: D,
    NonceStr: "".concat(D).concat(get_random_str()),
    "App-Id": '4ac490420ac63db4',
    "Device-Os": "web"
}
var M = {}
var l_c = 'a75846eb4ac490420ac63db46d2a03bf'
var h = function (t) {
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "a75846eb4ac490420ac63db46d2a03bf"
        , n = e + f(data) + f(t) + e;
    return n = d(n),
        n = v(n)
}

console.log(h(U, M, l_c))

