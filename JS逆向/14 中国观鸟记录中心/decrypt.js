
const CryptoJS = require('crypto-js');

function decrypt(a) {
        var key = '3583ec0257e2f4c8195eec7410ff1619'
        var iv = 'd93c0d5ec6352f20'
        var b = CryptoJS.enc.Utf8.parse(key);
        var c = CryptoJS.enc.Utf8.parse(iv);
        var d = CryptoJS.AES.decrypt(a, b, {
            iv: c,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return d.toString(CryptoJS.enc.Utf8)
    }