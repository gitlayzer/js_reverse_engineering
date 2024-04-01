var JSEncrypt = require("node-jsencrypt")
const CryptoJS = require('crypto-js');
const crypto = require('crypto');
/*
 a.params = {
                    b: t,
                    kiv: s
                }
 */

function getKiv() {
    var e = 16
    // void 0 === e && (e = 16); //下面运行和其实和e无关,可以直接指定e=16，看到random 就是随机字符串
    for (var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""), n = "", r = 0; r < e; r++) {
        n += t[Math.ceil(61 * Math.random())]
    }
    return n
}

/*
 M.mA)(n, {
                    iv: s
                })
 */
// decrypt = function(e, t) {
//             void 0 === e && (e = ""),
//             void 0 === t && (t = "");
//             var n = u()
//               , r = o.AES.encrypt(e.toString(), n.key, {
//                 iv: o.enc.Utf8.parse(t),
//                 mode: n.mode,
//                 padding: n.pad
//             });
//             return r = r.toString()
// }
var t_obj = {iv:getKiv()}
var data = '{"cityCode":101280600,"industryCode":"","curPage":1,"establishYears":"","registerCapitals":""}'

