window = global

function o(n) {
                t = "",
                ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function(n) {
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
                t = window["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
                    return o("0x" + t)
                });
                try {
                    return window["btoa"](t)
                } catch (n) {
                    return window["Buffer"]["from"](t)["toString"]("base64")
                }
            }
function get_analysis(t) {
    //var n; // undefined
    // f =false F为null s=575 F!=s 为true, 所以 s|| 后面的不执行，直接返回true
    // f || F != s || (n = (0, i[Wt])(m), s = c[x][k][Pt] = -(0, i[Wt])(l) || +new z[W] - a2 * n);
    var s =575
    var e, r = +new Date()- s - 1661224081041, a = [];
    return void 0 === t["params"] && (t["params"] = {}),
        window["Object"]["keys"](t["params"])["forEach"](function (n) {
            if (n == "analysis")
                return !1;
            t["params"]["hasOwnProperty"](n) && a["push"](t["params"][n])
        }),
        a = a["sort"]()["join"](""),
        a = getV(a),
        a = (a += "@#" + t["url"]["replace"](t["baseURL"], "")) + ("@#" + r) + ("@#" + 3),
        e = getV(h(a, "xyz517cda96efgh")),
    -1 == t["url"]["indexOf"]("analysis") && (t["url"] += (-1 != t["url"]["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + window["encodeURIComponent"](e)),
        t
}

var data = {
    "url": "/indexV2/getIndexRank",
    "method": "get",
    "headers": {
        "common": {
            "Accept": "application/json, text/plain, */*"
        },
        "delete": {},
        "get": {},
        "head": {},
        "post": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "put": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "patch": {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    },
    "params": {
        "setting": 0,
        "genre": "5000"
    },
    "baseURL": "https://api.qimai.cn",
    "transformRequest": [
        null
    ],
    "transformResponse": [
        null
    ],
    "timeout": 15000,
    "withCredentials": true,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1
}

console.log(get_analysis(data))