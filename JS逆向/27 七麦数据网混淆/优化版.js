window = global

function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function (n) {
            t += window["unescape"]("%u00" + n)
        });
    var t, e = t;
    return window["String"]["fromCharCode"](n)
}

function h(n, t) {
    // t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}

function getV(t) {
    t = window["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    try {
        return window["btoa"](t)
    } catch (n) {
        return window["Buffer"]["from"](t)["toString"]("base64")
    }
}

function get_analysis(url, params) {
    // 只用到了data 里的 url params 和 baseurl
    //var n; // undefined
    // f =false F为null s=575 F!=s 为true, 所以 s|| 后面的不执行，直接返回true
    // f || F != s || (n = (0, i[Wt])(m), s = c[x][k][Pt] = -(0, i[Wt])(l) || +new z[W] - a2 * n);
    var baseURL = "https://api.qimai.cn"
    var s = 575
    var e, r = +new Date() - s - 1661224081041, a = [];
    return void 0 === params && (params = {}),
        window["Object"]["keys"](params)["forEach"](function (n) {
            if (n == "analysis")
                return !1;
            params["hasOwnProperty"](n) && a["push"](params[n])
        }),
        a = a["sort"]()["join"](""),
        a = getV(a),
        a = (a += "@#" + url["replace"](baseURL, "")) + ("@#" + r) + ("@#" + 3),
        e = getV(h(a, "xyz517cda96efgh")),
    -1 == url["indexOf"]("analysis") && (url += (-1 != url["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + window["encodeURIComponent"](e)),
        //上面是针对构建好的analysis 对data里的url进行拼接，所以直接返回e 即可也就是构建好的analysis
        e
}

var url = "/indexV2/getIndexRank"
var params = {
    "setting": 0,
    "genre": "5000"
}
// 因为全站请求都有这个analysis，所以针对不同的url和params 获取不同的analysis
console.log(get_analysis(url, params))