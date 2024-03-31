`
注意 加载器末尾   , r = self["webpackChunkbbs_pc"] = self["webpackChunkbbs_pc"] || []; 这个会报错， 改成r=[]即可 r = [];
同时要手动加载目标函数 n(88086)
`

window = global;
location = {
    
    hostname : 'www.dxy.cn'
}
!(function() {
    var e = {

        88086: function(e, t, n) {
            var r = n(48764)["Buffer"];
            (function(t, n) {
                e.exports = n()
            }
            )(0, (function() {
                "use strict";
                function e(e, t, n) {
                    return t in e ? Object.defineProperty(e, t, {
                        value: n,
                        enumerable: !0,
                        configurable: !0,
                        writable: !0
                    }) : e[t] = n,
                    e
                }
                function t(t) {
                    for (var n = 1; n < arguments.length; n++) {
                        var r = null != arguments[n] ? arguments[n] : {}
                          , o = Object.keys(r);
                        "function" === typeof Object.getOwnPropertySymbols && (o = o.concat(Object.getOwnPropertySymbols(r).filter((function(e) {
                            return Object.getOwnPropertyDescriptor(r, e).enumerable
                        }
                        )))),
                        o.forEach((function(n) {
                            e(t, n, r[n])
                        }
                        ))
                    }
                    return t
                }
                function n(e, t) {
                    return t = {
                        exports: {}
                    },
                    e(t, t.exports),
                    t.exports
                }
                var o = n((function(e) {
                    (function() {
                        var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                          , n = {
                            rotl: function(e, t) {
                                return e << t | e >>> 32 - t
                            },
                            rotr: function(e, t) {
                                return e << 32 - t | e >>> t
                            },
                            endian: function(e) {
                                if (e.constructor == Number)
                                    return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                                for (var t = 0; t < e.length; t++)
                                    e[t] = n.endian(e[t]);
                                return e
                            },
                            randomBytes: function(e) {
                                for (var t = []; e > 0; e--)
                                    t.push(Math.floor(256 * Math.random()));
                                return t
                            },
                            bytesToWords: function(e) {
                                for (var t = [], n = 0, r = 0; n < e.length; n++,
                                r += 8)
                                    t[r >>> 5] |= e[n] << 24 - r % 32;
                                return t
                            },
                            wordsToBytes: function(e) {
                                for (var t = [], n = 0; n < 32 * e.length; n += 8)
                                    t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                                return t
                            },
                            bytesToHex: function(e) {
                                for (var t = [], n = 0; n < e.length; n++)
                                    t.push((e[n] >>> 4).toString(16)),
                                    t.push((15 & e[n]).toString(16));
                                return t.join("")
                            },
                            hexToBytes: function(e) {
                                for (var t = [], n = 0; n < e.length; n += 2)
                                    t.push(parseInt(e.substr(n, 2), 16));
                                return t
                            },
                            bytesToBase64: function(e) {
                                for (var n = [], r = 0; r < e.length; r += 3)
                                    for (var o = e[r] << 16 | e[r + 1] << 8 | e[r + 2], i = 0; i < 4; i++)
                                        8 * r + 6 * i <= 8 * e.length ? n.push(t.charAt(o >>> 6 * (3 - i) & 63)) : n.push("=");
                                return n.join("")
                            },
                            base64ToBytes: function(e) {
                                e = e.replace(/[^A-Z0-9+\/]/gi, "");
                                for (var n = [], r = 0, o = 0; r < e.length; o = ++r % 4)
                                    0 != o && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(r)) >>> 6 - 2 * o);
                                return n
                            }
                        };
                        e.exports = n
                    }
                    )()
                }
                ))
                  , i = {
                    utf8: {
                        stringToBytes: function(e) {
                            return i.bin.stringToBytes(unescape(encodeURIComponent(e)))
                        },
                        bytesToString: function(e) {
                            return decodeURIComponent(escape(i.bin.bytesToString(e)))
                        }
                    },
                    bin: {
                        stringToBytes: function(e) {
                            for (var t = [], n = 0; n < e.length; n++)
                                t.push(255 & e.charCodeAt(n));
                            return t
                        },
                        bytesToString: function(e) {
                            for (var t = [], n = 0; n < e.length; n++)
                                t.push(String.fromCharCode(e[n]));
                            return t.join("")
                        }
                    }
                }
                  , a = i
                  , s = n((function(e) {
                    (function() {
                        var t = o
                          , n = a.utf8
                          , i = a.bin
                          , s = function(e) {
                            e.constructor == String ? e = n.stringToBytes(e) : "undefined" !== typeof r && "function" == typeof r.isBuffer && r.isBuffer(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
                            var o = t.bytesToWords(e)
                              , i = 8 * e.length
                              , a = []
                              , s = 1732584193
                              , u = -271733879
                              , c = -1732584194
                              , l = 271733878
                              , f = -1009589776;
                            o[i >> 5] |= 128 << 24 - i % 32,
                            o[15 + (i + 64 >>> 9 << 4)] = i;
                            for (var d = 0; d < o.length; d += 16) {
                                for (var p = s, h = u, v = c, y = l, g = f, m = 0; m < 80; m++) {
                                    if (m < 16)
                                        a[m] = o[d + m];
                                    else {
                                        var b = a[m - 3] ^ a[m - 8] ^ a[m - 14] ^ a[m - 16];
                                        a[m] = b << 1 | b >>> 31
                                    }
                                    var _ = (s << 5 | s >>> 27) + f + (a[m] >>> 0) + (m < 20 ? 1518500249 + (u & c | ~u & l) : m < 40 ? 1859775393 + (u ^ c ^ l) : m < 60 ? (u & c | u & l | c & l) - 1894007588 : (u ^ c ^ l) - 899497514);
                                    f = l,
                                    l = c,
                                    c = u << 30 | u >>> 2,
                                    u = s,
                                    s = _
                                }
                                s += p,
                                u += h,
                                c += v,
                                l += y,
                                f += g
                            }
                            return [s, u, c, l, f]
                        }
                          , u = function(e, n) {
                            var r = t.wordsToBytes(s(e));
                            return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r)
                        };
                        u._blocksize = 16,
                        u._digestsize = 20,
                        e.exports = u
                    }
                    )()
                }
                ));
                function u() {
                    for (var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 8, t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "alphabet", n = "", r = {
                        alphabet: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                        number: "0123456789"
                    }[t], o = 0; o < e; o++)
                        n += r.charAt(Math.floor(Math.random() * r.length));
                    return n
                }
                var c = "10f6cf80184377cd5487b4746a8a67da17540449fa40b408f13ccdd3d3059cb394c0e1569043eed2"
                  , l = 0
                  , f = function() {
                    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
                      , n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : c
                      , r = arguments.length > 2 && void 0 !== arguments[2] && arguments[2]
                      , o = t({}, e)
                      , i = {
                        appSignKey: n
                    }
                      , a = Date.now();
                    e.serverTimestamp && !l && (l = e.serverTimestamp - a),
                    o.timestamp = a + l,
                    o.noncestr = u(8, "number");
                    var f = Object.keys(o).filter((function(e) {
                        return void 0 != o[e] && "" !== o[e] || (delete o[e],
                        !1)
                    }
                    )).concat("appSignKey").sort().map((function(e) {
                        var t = i[e] || (void 0 == o[e] ? "" : o[e]);
                        return "".concat(e, "=").concat(t)
                    }
                    )).join("&");
                    return r && console.log("sign", e, f),
                    o.sign = s(f),
                    o
                };
                window.f = f
                function d(e, t) {
                    t || (t = window.location.href),
                    e = e.replace(/[\[\]]/g, "\\$&");
                    var n = new RegExp("[?&]".concat(e, "(=([^&#]*)|&|#|$)"))
                      , r = n.exec(t);
                    return r ? r[2] ? decodeURIComponent(r[2].replace(/\+/g, " ")) : "" : null
                }
                var p, h, v, y, g, m = Object.prototype.hasOwnProperty, b = function() {
                    for (var e = [], t = 0; t < 256; ++t)
                        e.push("%" + ((t < 16 ? "0" : "") + t.toString(16)).toUpperCase());
                    return e
                }(), _ = function(e) {
                    while (e.length > 1) {
                        var t = e.pop()
                          , n = t.obj[t.prop];
                        if (Array.isArray(n)) {
                            for (var r = [], o = 0; o < n.length; ++o)
                                "undefined" !== typeof n[o] && r.push(n[o]);
                            t.obj[t.prop] = r
                        }
                    }
                }, k = function(e, t) {
                    for (var n = t && t.plainObjects ? Object.create(null) : {}, r = 0; r < e.length; ++r)
                        "undefined" !== typeof e[r] && (n[r] = e[r]);
                    return n
                }, w = function e(t, n, r) {
                    if (!n)
                        return t;
                    if ("object" !== typeof n) {
                        if (Array.isArray(t))
                            t.push(n);
                        else {
                            if ("object" !== typeof t)
                                return [t, n];
                            (r && (r.plainObjects || r.allowPrototypes) || !m.call(Object.prototype, n)) && (t[n] = !0)
                        }
                        return t
                    }
                    if ("object" !== typeof t)
                        return [t].concat(n);
                    var o = t;
                    return Array.isArray(t) && !Array.isArray(n) && (o = k(t, r)),
                    Array.isArray(t) && Array.isArray(n) ? (n.forEach((function(n, o) {
                        m.call(t, o) ? t[o] && "object" === typeof t[o] ? t[o] = e(t[o], n, r) : t.push(n) : t[o] = n
                    }
                    )),
                    t) : Object.keys(n).reduce((function(t, o) {
                        var i = n[o];
                        return m.call(t, o) ? t[o] = e(t[o], i, r) : t[o] = i,
                        t
                    }
                    ), o)
                }, E = function(e, t) {
                    return Object.keys(t).reduce((function(e, n) {
                        return e[n] = t[n],
                        e
                    }
                    ), e)
                }, M = function(e, t, n) {
                    var r = e.replace(/\+/g, " ");
                    if ("iso-8859-1" === n)
                        return r.replace(/%[0-9a-f]{2}/gi, unescape);
                    try {
                        return decodeURIComponent(r)
                    } catch (o) {
                        return r
                    }
                }, C = function(e, t, n) {
                    if (0 === e.length)
                        return e;
                    var r = "string" === typeof e ? e : String(e);
                    if ("iso-8859-1" === n)
                        return escape(r).replace(/%u[0-9a-f]{4}/gi, (function(e) {
                            return "%26%23" + parseInt(e.slice(2), 16) + "%3B"
                        }
                        ));
                    for (var o = "", i = 0; i < r.length; ++i) {
                        var a = r.charCodeAt(i);
                        45 === a || 46 === a || 95 === a || 126 === a || a >= 48 && a <= 57 || a >= 65 && a <= 90 || a >= 97 && a <= 122 ? o += r.charAt(i) : a < 128 ? o += b[a] : a < 2048 ? o += b[192 | a >> 6] + b[128 | 63 & a] : a < 55296 || a >= 57344 ? o += b[224 | a >> 12] + b[128 | a >> 6 & 63] + b[128 | 63 & a] : (i += 1,
                        a = 65536 + ((1023 & a) << 10 | 1023 & r.charCodeAt(i)),
                        o += b[240 | a >> 18] + b[128 | a >> 12 & 63] + b[128 | a >> 6 & 63] + b[128 | 63 & a])
                    }
                    return o
                }, T = function(e) {
                    for (var t = [{
                        obj: {
                            o: e
                        },
                        prop: "o"
                    }], n = [], r = 0; r < t.length; ++r)
                        for (var o = t[r], i = o.obj[o.prop], a = Object.keys(i), s = 0; s < a.length; ++s) {
                            var u = a[s]
                              , c = i[u];
                            "object" === typeof c && null !== c && -1 === n.indexOf(c) && (t.push({
                                obj: i,
                                prop: u
                            }),
                            n.push(c))
                        }
                    return _(t),
                    e
                }, S = function(e) {
                    return "[object RegExp]" === Object.prototype.toString.call(e)
                }, I = function(e) {
                    return null !== e && "undefined" !== typeof e && !!(e.constructor && e.constructor.isBuffer && e.constructor.isBuffer(e))
                }, O = function(e, t) {
                    return [].concat(e, t)
                }, A = {
                    arrayToObject: k,
                    assign: E,
                    combine: O,
                    compact: T,
                    decode: M,
                    encode: C,
                    isBuffer: I,
                    isRegExp: S,
                    merge: w
                }, x = String.prototype.replace, N = /%20/g, D = {
                    default: "RFC3986",
                    formatters: {
                        RFC1738: function(e) {
                            return x.call(e, N, "+")
                        },
                        RFC3986: function(e) {
                            return e
                        }
                    },
                    RFC1738: "RFC1738",
                    RFC3986: "RFC3986"
                }, R = {
                    brackets: function(e) {
                        return e + "[]"
                    },
                    indices: function(e, t) {
                        return e + "[" + t + "]"
                    },
                    repeat: function(e) {
                        return e
                    }
                }, P = Array.isArray, L = Array.prototype.push, U = function(e, t) {
                    L.apply(e, P(t) ? t : [t])
                }, F = Date.prototype.toISOString, G = {
                    addQueryPrefix: !1,
                    allowDots: !1,
                    charset: "utf-8",
                    charsetSentinel: !1,
                    delimiter: "&",
                    encode: !0,
                    encoder: A.encode,
                    encodeValuesOnly: !1,
                    indices: !1,
                    serializeDate: function(e) {
                        return F.call(e)
                    },
                    skipNulls: !1,
                    strictNullHandling: !1
                }, j = function e(t, n, r, o, i, a, s, u, c, l, f, d, p) {
                    var h = t;
                    if ("function" === typeof s ? h = s(n, h) : h instanceof Date && (h = l(h)),
                    null === h) {
                        if (o)
                            return a && !d ? a(n, G.encoder, p) : n;
                        h = ""
                    }
                    if ("string" === typeof h || "number" === typeof h || "boolean" === typeof h || A.isBuffer(h)) {
                        if (a) {
                            var v = d ? n : a(n, G.encoder, p);
                            return [f(v) + "=" + f(a(h, G.encoder, p))]
                        }
                        return [f(n) + "=" + f(String(h))]
                    }
                    var y, g = [];
                    if ("undefined" === typeof h)
                        return g;
                    if (Array.isArray(s))
                        y = s;
                    else {
                        var m = Object.keys(h);
                        y = u ? m.sort(u) : m
                    }
                    for (var b = 0; b < y.length; ++b) {
                        var _ = y[b];
                        i && null === h[_] || (Array.isArray(h) ? U(g, e(h[_], r(n, _), r, o, i, a, s, u, c, l, f, d, p)) : U(g, e(h[_], n + (c ? "." + _ : "[" + _ + "]"), r, o, i, a, s, u, c, l, f, d, p)))
                    }
                    return g
                }, q = function(e, t) {
                    var n = e
                      , r = t ? A.assign({}, t) : {};
                    if (null !== r.encoder && void 0 !== r.encoder && "function" !== typeof r.encoder)
                        throw new TypeError("Encoder has to be a function.");
                    var o = "undefined" === typeof r.delimiter ? G.delimiter : r.delimiter
                      , i = "boolean" === typeof r.strictNullHandling ? r.strictNullHandling : G.strictNullHandling
                      , a = "boolean" === typeof r.skipNulls ? r.skipNulls : G.skipNulls
                      , s = "boolean" === typeof r.encode ? r.encode : G.encode
                      , u = "function" === typeof r.encoder ? r.encoder : G.encoder
                      , c = "function" === typeof r.sort ? r.sort : null
                      , l = "undefined" === typeof r.allowDots ? G.allowDots : !!r.allowDots
                      , f = "function" === typeof r.serializeDate ? r.serializeDate : G.serializeDate
                      , d = "boolean" === typeof r.encodeValuesOnly ? r.encodeValuesOnly : G.encodeValuesOnly
                      , p = r.charset || G.charset;
                    if ("undefined" !== typeof r.charset && "utf-8" !== r.charset && "iso-8859-1" !== r.charset)
                        throw new Error("The charset option must be either utf-8, iso-8859-1, or undefined");
                    if ("undefined" === typeof r.format)
                        r.format = D["default"];
                    else if (!Object.prototype.hasOwnProperty.call(D.formatters, r.format))
                        throw new TypeError("Unknown format option provided.");
                    var h, v, y = D.formatters[r.format];
                    "function" === typeof r.filter ? (v = r.filter,
                    n = v("", n)) : Array.isArray(r.filter) && (v = r.filter,
                    h = v);
                    var g, m = [];
                    if ("object" !== typeof n || null === n)
                        return "";
                    g = r.arrayFormat in R ? r.arrayFormat : "indices"in r ? r.indices ? "indices" : "repeat" : "indices";
                    var b = R[g];
                    h || (h = Object.keys(n)),
                    c && h.sort(c);
                    for (var _ = 0; _ < h.length; ++_) {
                        var k = h[_];
                        a && null === n[k] || U(m, j(n[k], k, b, i, a, s ? u : null, v, c, l, f, y, d, p))
                    }
                    var w = m.join(o)
                      , E = !0 === r.addQueryPrefix ? "?" : "";
                    return r.charsetSentinel && (E += "iso-8859-1" === p ? "utf8=%26%2310003%3B&" : "utf8=%E2%9C%93&"),
                    w.length > 0 ? E + w : ""
                }, Z = Object.prototype.hasOwnProperty, B = {
                    allowDots: !1,
                    allowPrototypes: !1,
                    arrayLimit: 20,
                    charset: "utf-8",
                    charsetSentinel: !1,
                    decoder: A.decode,
                    delimiter: "&",
                    depth: 5,
                    ignoreQueryPrefix: !1,
                    interpretNumericEntities: !1,
                    parameterLimit: 1e3,
                    parseArrays: !0,
                    plainObjects: !1,
                    strictNullHandling: !1
                }, V = function(e) {
                    return e.replace(/&#(\d+);/g, (function(e, t) {
                        return String.fromCharCode(parseInt(t, 10))
                    }
                    ))
                }, H = "utf8=%26%2310003%3B", W = "utf8=%E2%9C%93", z = function(e, t) {
                    var n, r = {}, o = t.ignoreQueryPrefix ? e.replace(/^\?/, "") : e, i = t.parameterLimit === 1 / 0 ? void 0 : t.parameterLimit, a = o.split(t.delimiter, i), s = -1, u = t.charset;
                    if (t.charsetSentinel)
                        for (n = 0; n < a.length; ++n)
                            0 === a[n].indexOf("utf8=") && (a[n] === W ? u = "utf-8" : a[n] === H && (u = "iso-8859-1"),
                            s = n,
                            n = a.length);
                    for (n = 0; n < a.length; ++n)
                        if (n !== s) {
                            var c, l, f = a[n], d = f.indexOf("]="), p = -1 === d ? f.indexOf("=") : d + 1;
                            -1 === p ? (c = t.decoder(f, B.decoder, u),
                            l = t.strictNullHandling ? null : "") : (c = t.decoder(f.slice(0, p), B.decoder, u),
                            l = t.decoder(f.slice(p + 1), B.decoder, u)),
                            l && t.interpretNumericEntities && "iso-8859-1" === u && (l = V(l)),
                            Z.call(r, c) ? r[c] = A.combine(r[c], l) : r[c] = l
                        }
                    return r
                }, K = function(e, t, n) {
                    for (var r = t, o = e.length - 1; o >= 0; --o) {
                        var i, a = e[o];
                        if ("[]" === a && n.parseArrays)
                            i = [].concat(r);
                        else {
                            i = n.plainObjects ? Object.create(null) : {};
                            var s = "[" === a.charAt(0) && "]" === a.charAt(a.length - 1) ? a.slice(1, -1) : a
                              , u = parseInt(s, 10);
                            n.parseArrays || "" !== s ? !isNaN(u) && a !== s && String(u) === s && u >= 0 && n.parseArrays && u <= n.arrayLimit ? (i = [],
                            i[u] = r) : i[s] = r : i = {
                                0: r
                            }
                        }
                        r = i
                    }
                    return r
                }, Y = function(e, t, n) {
                    if (e) {
                        var r = n.allowDots ? e.replace(/\.([^.[]+)/g, "[$1]") : e
                          , o = /(\[[^[\]]*])/
                          , i = /(\[[^[\]]*])/g
                          , a = o.exec(r)
                          , s = a ? r.slice(0, a.index) : r
                          , u = [];
                        if (s) {
                            if (!n.plainObjects && Z.call(Object.prototype, s) && !n.allowPrototypes)
                                return;
                            u.push(s)
                        }
                        var c = 0;
                        while (null !== (a = i.exec(r)) && c < n.depth) {
                            if (c += 1,
                            !n.plainObjects && Z.call(Object.prototype, a[1].slice(1, -1)) && !n.allowPrototypes)
                                return;
                            u.push(a[1])
                        }
                        return a && u.push("[" + r.slice(a.index) + "]"),
                        K(u, t, n)
                    }
                }, $ = function(e, t) {
                    var n = t ? A.assign({}, t) : {};
                    if (null !== n.decoder && void 0 !== n.decoder && "function" !== typeof n.decoder)
                        throw new TypeError("Decoder has to be a function.");
                    if (n.ignoreQueryPrefix = !0 === n.ignoreQueryPrefix,
                    n.delimiter = "string" === typeof n.delimiter || A.isRegExp(n.delimiter) ? n.delimiter : B.delimiter,
                    n.depth = "number" === typeof n.depth ? n.depth : B.depth,
                    n.arrayLimit = "number" === typeof n.arrayLimit ? n.arrayLimit : B.arrayLimit,
                    n.parseArrays = !1 !== n.parseArrays,
                    n.decoder = "function" === typeof n.decoder ? n.decoder : B.decoder,
                    n.allowDots = "undefined" === typeof n.allowDots ? B.allowDots : !!n.allowDots,
                    n.plainObjects = "boolean" === typeof n.plainObjects ? n.plainObjects : B.plainObjects,
                    n.allowPrototypes = "boolean" === typeof n.allowPrototypes ? n.allowPrototypes : B.allowPrototypes,
                    n.parameterLimit = "number" === typeof n.parameterLimit ? n.parameterLimit : B.parameterLimit,
                    n.strictNullHandling = "boolean" === typeof n.strictNullHandling ? n.strictNullHandling : B.strictNullHandling,
                    "undefined" !== typeof n.charset && "utf-8" !== n.charset && "iso-8859-1" !== n.charset)
                        throw new Error("The charset option must be either utf-8, iso-8859-1, or undefined");
                    if ("undefined" === typeof n.charset && (n.charset = B.charset),
                    "" === e || null === e || "undefined" === typeof e)
                        return n.plainObjects ? Object.create(null) : {};
                    for (var r = "string" === typeof e ? z(e, n) : e, o = n.plainObjects ? Object.create(null) : {}, i = Object.keys(r), a = 0; a < i.length; ++a) {
                        var s = i[a]
                          , u = Y(s, r[s], n);
                        o = A.merge(o, u, n)
                    }
                    return A.compact(o)
                }, X = {
                    formats: D,
                    parse: $,
                    stringify: q
                }, J = X.stringify, Q = ["sr", "nm", "pt", "dt", "pd", "from", "qrcode"], ee = function() {
                    return /\.net$/.test(location.hostname)
                }, te = function() {
                    var e = Q
                      , n = e.reduce((function(e, t) {
                        return d(t) && (e[t] = d(t)),
                        e
                    }
                    ), {})
                      , r = window && window.location && window.location.href || void 0;
                    return t({
                        from: r
                    }, n)
                }, ne = "dxyer", re = "drugs", oe = "exam", ie = (p = {},
                e(p, ne, /^dxy-dxyer/),
                e(p, re, /^dxy-drugs/),
                e(p, oe, /^dxy-inderal/),
                p), ae = (h = {},
                e(h, ne, ee() ? "https://app.dxy.net/dxyer/" : "https://app.dxy.cn/dxyer/"),
                e(h, re, ee() ? "https://app.dxy.net/drugs/" : "https://app.dxy.cn/drugs/"),
                e(h, oe, ee() ? "https://app.dxy.net/inderal/" : "https://app.dxy.cn/inderal/"),
                h), se = (v = {},
                e(v, ne, "cn.dxy.idxyer"),
                e(v, re, "cn.dxy.medicinehelper"),
                e(v, oe, "cn.dxy.inderal"),
                y = {},
                e(y, ne, "\u4e01\u9999\u56ed"),
                e(y, re, "\u7528\u836f\u52a9\u624b"),
                e(y, oe, "\u4e01\u9999\u533b\u8003"),
                y), ue = (g = {},
                e(g, ne, ee() ? "https://app.dxy.net/dxyer.htm" : "https://app.dxy.cn/dxyer.htm"),
                e(g, re, ee() ? "https://app.dxy.net/drugs.htm" : "https://app.dxy.cn/drugs.htm"),
                e(g, oe, ee() ? "https://app.dxy.net/inderal.htm" : "https://app.dxy.cn/inderal.htm"),
                g), ce = function(e) {
                    for (var t in ie)
                        if (ie[t].test(e))
                            return t
                }, le = function() {
                    return navigator && navigator.userAgent && /MicroMessenger/.test(navigator.userAgent)
                }, fe = function() {
                    return navigator && navigator.userAgent && /iPhone/.test(navigator.userAgent)
                }, de = function() {
                    return navigator && navigator.userAgent && /Safari/.test(navigator.userAgent) && !/Chrome/.test(navigator.userAgent)
                }, pe = function() {
                    return navigator && navigator.userAgent && /Weibo/.test(navigator.userAgent)
                }, he = function() {
                    return navigator && navigator.userAgent && /dxy/.test(navigator.userAgent)
                }, ve = function() {
                    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : -1;
                    function t(e) {
                        var t = !1
                          , n = Date.now()
                          , r = setInterval((function() {
                            (Date.now() - n > 350 || document.hidden || "hidden" === document.visibilityState) && (!t && e("1 seconds" + document.hidden),
                            t = !0,
                            clearInterval(r),
                            a()),
                            n = Date.now()
                        }
                        ), 100);
                        function o() {
                            !t && e("visibilitychange"),
                            t = !0,
                            clearInterval(r),
                            a()
                        }
                        function i(n) {
                            !t && e("blur"),
                            t = !0,
                            clearInterval(r),
                            a()
                        }
                        function a() {
                            document.removeEventListener("visibilitychange", o),
                            window.removeEventListener("blur", i),
                            document.body.removeEventListener("blur", i),
                            window.removeEventListener("unload", i)
                        }
                        document.addEventListener("visibilitychange", o, !1),
                        window.addEventListener("blur", i, !1),
                        document.body.addEventListener("blur", i, !1),
                        window.addEventListener("unload", i, !1)
                    }
                    return new Promise((function(n) {
                        var r = !1;
                        t((function(e) {
                            r || (r = !0,
                            n(!0))
                        }
                        )),
                        e > 0 && setTimeout((function() {
                            r || (r = !0,
                            n(!1))
                        }
                        ), e)
                    }
                    ))
                }, ye = function() {
                    return !(!de() && !fe() || le() || he())
                }, ge = function(e) {
                    location.href = e
                }, me = function(e) {
                    var t = ce(e)
                      , n = e.replace(/.*:\/\//, "");
                    return ae[t] + (n || "index")
                }, be = function(e) {
                    var t = ce(e)
                      , n = e.replace(/.*:\/\//, "");
                    location.href = ae[t] + (n || "index")
                }, _e = function(e, t) {
                    return ce(e) ? (setTimeout((function() {
                        ye() ? be(e) : ge(e)
                    }
                    ), 10),
                    ve(t)) : Promise.resolve(!1)
                };
                function ke(e) {
                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                      , r = t({}, te(), n.params)
                      , o = "".concat(e).concat(/\?/.test(e) ? "&" : "?").concat(J(r))
                      , i = ce(e)
                      , a = (se[i],
                    (ue[i] || "https://app.dxy.cn") + "?_scheme=".concat(encodeURIComponent(o), "&").concat(J(r)));
                    return new Promise((function(e) {
                        if (pe())
                            return window.location.href = "https://assets.dxycdn.com/gitrepo/tod-assets/output/default/launchapp/page.htm?t=".concat(Date.now(), "&scheme=").concat(encodeURIComponent(o), "&link=").concat(encodeURIComponent(me(o)));
                        le() ? (fe() && i ? be(o) : location.href = a,
                        e(!1)) : _e(o, n.timeout || 2e3).then((function(t) {
                            t || !1 === n.redirect || (location.href = a),
                            e(t)
                        }
                        ))
                    }
                    ))
                }
                ke.scheme = _e;
                var we = {
                    sign: f,
                    openScheme: ke
                };
                return we
            }
            ))
        },
         48764: function(e, t, n) {
            "use strict";
            var r = n(79742)
              , o = n(80645)
              , i = n(87300);
            function a() {
                try {
                    var e = new Uint8Array(1);
                    return e.__proto__ = {
                        __proto__: Uint8Array.prototype,
                        foo: function() {
                            return 42
                        }
                    },
                    42 === e.foo() && "function" === typeof e.subarray && 0 === e.subarray(1, 1).byteLength
                } catch (t) {
                    return !1
                }
            }
            function s() {
                return c.TYPED_ARRAY_SUPPORT ? 2147483647 : 1073741823
            }
            function u(e, t) {
                if (s() < t)
                    throw new RangeError("Invalid typed array length");
                return c.TYPED_ARRAY_SUPPORT ? (e = new Uint8Array(t),
                e.__proto__ = c.prototype) : (null === e && (e = new c(t)),
                e.length = t),
                e
            }
            function c(e, t, n) {
                if (!c.TYPED_ARRAY_SUPPORT && !(this instanceof c))
                    return new c(e,t,n);
                if ("number" === typeof e) {
                    if ("string" === typeof t)
                        throw new Error("If encoding is specified then the first argument must be a string");
                    return p(this, e)
                }
                return l(this, e, t, n)
            }
            function l(e, t, n, r) {
                if ("number" === typeof t)
                    throw new TypeError('"value" argument must not be a number');
                return "undefined" !== typeof ArrayBuffer && t instanceof ArrayBuffer ? y(e, t, n, r) : "string" === typeof t ? h(e, t, n) : g(e, t)
            }
            function f(e) {
                if ("number" !== typeof e)
                    throw new TypeError('"size" argument must be a number');
                if (e < 0)
                    throw new RangeError('"size" argument must not be negative')
            }
            function d(e, t, n, r) {
                return f(t),
                t <= 0 ? u(e, t) : void 0 !== n ? "string" === typeof r ? u(e, t).fill(n, r) : u(e, t).fill(n) : u(e, t)
            }
            function p(e, t) {
                if (f(t),
                e = u(e, t < 0 ? 0 : 0 | m(t)),
                !c.TYPED_ARRAY_SUPPORT)
                    for (var n = 0; n < t; ++n)
                        e[n] = 0;
                return e
            }
            function h(e, t, n) {
                if ("string" === typeof n && "" !== n || (n = "utf8"),
                !c.isEncoding(n))
                    throw new TypeError('"encoding" must be a valid string encoding');
                var r = 0 | _(t, n);
                e = u(e, r);
                var o = e.write(t, n);
                return o !== r && (e = e.slice(0, o)),
                e
            }
            function v(e, t) {
                var n = t.length < 0 ? 0 : 0 | m(t.length);
                e = u(e, n);
                for (var r = 0; r < n; r += 1)
                    e[r] = 255 & t[r];
                return e
            }
            function y(e, t, n, r) {
                if (t.byteLength,
                n < 0 || t.byteLength < n)
                    throw new RangeError("'offset' is out of bounds");
                if (t.byteLength < n + (r || 0))
                    throw new RangeError("'length' is out of bounds");
                return t = void 0 === n && void 0 === r ? new Uint8Array(t) : void 0 === r ? new Uint8Array(t,n) : new Uint8Array(t,n,r),
                c.TYPED_ARRAY_SUPPORT ? (e = t,
                e.__proto__ = c.prototype) : e = v(e, t),
                e
            }
            function g(e, t) {
                if (c.isBuffer(t)) {
                    var n = 0 | m(t.length);
                    return e = u(e, n),
                    0 === e.length ? e : (t.copy(e, 0, 0, n),
                    e)
                }
                if (t) {
                    if ("undefined" !== typeof ArrayBuffer && t.buffer instanceof ArrayBuffer || "length"in t)
                        return "number" !== typeof t.length || te(t.length) ? u(e, 0) : v(e, t);
                    if ("Buffer" === t.type && i(t.data))
                        return v(e, t.data)
                }
                throw new TypeError("First argument must be a string, Buffer, ArrayBuffer, Array, or array-like object.")
            }
            function m(e) {
                if (e >= s())
                    throw new RangeError("Attempt to allocate Buffer larger than maximum size: 0x" + s().toString(16) + " bytes");
                return 0 | e
            }
            function b(e) {
                return +e != e && (e = 0),
                c.alloc(+e)
            }
            function _(e, t) {
                if (c.isBuffer(e))
                    return e.length;
                if ("undefined" !== typeof ArrayBuffer && "function" === typeof ArrayBuffer.isView && (ArrayBuffer.isView(e) || e instanceof ArrayBuffer))
                    return e.byteLength;
                "string" !== typeof e && (e = "" + e);
                var n = e.length;
                if (0 === n)
                    return 0;
                for (var r = !1; ; )
                    switch (t) {
                    case "ascii":
                    case "latin1":
                    case "binary":
                        return n;
                    case "utf8":
                    case "utf-8":
                    case void 0:
                        return $(e).length;
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return 2 * n;
                    case "hex":
                        return n >>> 1;
                    case "base64":
                        return Q(e).length;
                    default:
                        if (r)
                            return $(e).length;
                        t = ("" + t).toLowerCase(),
                        r = !0
                    }
            }
            function k(e, t, n) {
                var r = !1;
                if ((void 0 === t || t < 0) && (t = 0),
                t > this.length)
                    return "";
                if ((void 0 === n || n > this.length) && (n = this.length),
                n <= 0)
                    return "";
                if (n >>>= 0,
                t >>>= 0,
                n <= t)
                    return "";
                e || (e = "utf8");
                while (1)
                    switch (e) {
                    case "hex":
                        return U(this, t, n);
                    case "utf8":
                    case "utf-8":
                        return N(this, t, n);
                    case "ascii":
                        return P(this, t, n);
                    case "latin1":
                    case "binary":
                        return L(this, t, n);
                    case "base64":
                        return x(this, t, n);
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return F(this, t, n);
                    default:
                        if (r)
                            throw new TypeError("Unknown encoding: " + e);
                        e = (e + "").toLowerCase(),
                        r = !0
                    }
            }
            function w(e, t, n) {
                var r = e[t];
                e[t] = e[n],
                e[n] = r
            }
            function E(e, t, n, r, o) {
                if (0 === e.length)
                    return -1;
                if ("string" === typeof n ? (r = n,
                n = 0) : n > 2147483647 ? n = 2147483647 : n < -2147483648 && (n = -2147483648),
                n = +n,
                isNaN(n) && (n = o ? 0 : e.length - 1),
                n < 0 && (n = e.length + n),
                n >= e.length) {
                    if (o)
                        return -1;
                    n = e.length - 1
                } else if (n < 0) {
                    if (!o)
                        return -1;
                    n = 0
                }
                if ("string" === typeof t && (t = c.from(t, r)),
                c.isBuffer(t))
                    return 0 === t.length ? -1 : M(e, t, n, r, o);
                if ("number" === typeof t)
                    return t &= 255,
                    c.TYPED_ARRAY_SUPPORT && "function" === typeof Uint8Array.prototype.indexOf ? o ? Uint8Array.prototype.indexOf.call(e, t, n) : Uint8Array.prototype.lastIndexOf.call(e, t, n) : M(e, [t], n, r, o);
                throw new TypeError("val must be string, number or Buffer")
            }
            function M(e, t, n, r, o) {
                var i, a = 1, s = e.length, u = t.length;
                if (void 0 !== r && (r = String(r).toLowerCase(),
                "ucs2" === r || "ucs-2" === r || "utf16le" === r || "utf-16le" === r)) {
                    if (e.length < 2 || t.length < 2)
                        return -1;
                    a = 2,
                    s /= 2,
                    u /= 2,
                    n /= 2
                }
                function c(e, t) {
                    return 1 === a ? e[t] : e.readUInt16BE(t * a)
                }
                if (o) {
                    var l = -1;
                    for (i = n; i < s; i++)
                        if (c(e, i) === c(t, -1 === l ? 0 : i - l)) {
                            if (-1 === l && (l = i),
                            i - l + 1 === u)
                                return l * a
                        } else
                            -1 !== l && (i -= i - l),
                            l = -1
                } else
                    for (n + u > s && (n = s - u),
                    i = n; i >= 0; i--) {
                        for (var f = !0, d = 0; d < u; d++)
                            if (c(e, i + d) !== c(t, d)) {
                                f = !1;
                                break
                            }
                        if (f)
                            return i
                    }
                return -1
            }
            function C(e, t, n, r) {
                n = Number(n) || 0;
                var o = e.length - n;
                r ? (r = Number(r),
                r > o && (r = o)) : r = o;
                var i = t.length;
                if (i % 2 !== 0)
                    throw new TypeError("Invalid hex string");
                r > i / 2 && (r = i / 2);
                for (var a = 0; a < r; ++a) {
                    var s = parseInt(t.substr(2 * a, 2), 16);
                    if (isNaN(s))
                        return a;
                    e[n + a] = s
                }
                return a
            }
            function T(e, t, n, r) {
                return ee($(t, e.length - n), e, n, r)
            }
            function S(e, t, n, r) {
                return ee(X(t), e, n, r)
            }
            function I(e, t, n, r) {
                return S(e, t, n, r)
            }
            function O(e, t, n, r) {
                return ee(Q(t), e, n, r)
            }
            function A(e, t, n, r) {
                return ee(J(t, e.length - n), e, n, r)
            }
            function x(e, t, n) {
                return 0 === t && n === e.length ? r.fromByteArray(e) : r.fromByteArray(e.slice(t, n))
            }
            function N(e, t, n) {
                n = Math.min(e.length, n);
                var r = []
                  , o = t;
                while (o < n) {
                    var i, a, s, u, c = e[o], l = null, f = c > 239 ? 4 : c > 223 ? 3 : c > 191 ? 2 : 1;
                    if (o + f <= n)
                        switch (f) {
                        case 1:
                            c < 128 && (l = c);
                            break;
                        case 2:
                            i = e[o + 1],
                            128 === (192 & i) && (u = (31 & c) << 6 | 63 & i,
                            u > 127 && (l = u));
                            break;
                        case 3:
                            i = e[o + 1],
                            a = e[o + 2],
                            128 === (192 & i) && 128 === (192 & a) && (u = (15 & c) << 12 | (63 & i) << 6 | 63 & a,
                            u > 2047 && (u < 55296 || u > 57343) && (l = u));
                            break;
                        case 4:
                            i = e[o + 1],
                            a = e[o + 2],
                            s = e[o + 3],
                            128 === (192 & i) && 128 === (192 & a) && 128 === (192 & s) && (u = (15 & c) << 18 | (63 & i) << 12 | (63 & a) << 6 | 63 & s,
                            u > 65535 && u < 1114112 && (l = u))
                        }
                    null === l ? (l = 65533,
                    f = 1) : l > 65535 && (l -= 65536,
                    r.push(l >>> 10 & 1023 | 55296),
                    l = 56320 | 1023 & l),
                    r.push(l),
                    o += f
                }
                return R(r)
            }
            t.Buffer = c,
            t.SlowBuffer = b,
            t.INSPECT_MAX_BYTES = 50,
            c.TYPED_ARRAY_SUPPORT = void 0 !== n.g.TYPED_ARRAY_SUPPORT ? n.g.TYPED_ARRAY_SUPPORT : a(),
            t.kMaxLength = s(),
            c.poolSize = 8192,
            c._augment = function(e) {
                return e.__proto__ = c.prototype,
                e
            }
            ,
            c.from = function(e, t, n) {
                return l(null, e, t, n)
            }
            ,
            c.TYPED_ARRAY_SUPPORT && (c.prototype.__proto__ = Uint8Array.prototype,
            c.__proto__ = Uint8Array,
            "undefined" !== typeof Symbol && Symbol.species && c[Symbol.species] === c && Object.defineProperty(c, Symbol.species, {
                value: null,
                configurable: !0
            })),
            c.alloc = function(e, t, n) {
                return d(null, e, t, n)
            }
            ,
            c.allocUnsafe = function(e) {
                return p(null, e)
            }
            ,
            c.allocUnsafeSlow = function(e) {
                return p(null, e)
            }
            ,
            c.isBuffer = function(e) {
                return !(null == e || !e._isBuffer)
            }
            ,
            c.compare = function(e, t) {
                if (!c.isBuffer(e) || !c.isBuffer(t))
                    throw new TypeError("Arguments must be Buffers");
                if (e === t)
                    return 0;
                for (var n = e.length, r = t.length, o = 0, i = Math.min(n, r); o < i; ++o)
                    if (e[o] !== t[o]) {
                        n = e[o],
                        r = t[o];
                        break
                    }
                return n < r ? -1 : r < n ? 1 : 0
            }
            ,
            c.isEncoding = function(e) {
                switch (String(e).toLowerCase()) {
                case "hex":
                case "utf8":
                case "utf-8":
                case "ascii":
                case "latin1":
                case "binary":
                case "base64":
                case "ucs2":
                case "ucs-2":
                case "utf16le":
                case "utf-16le":
                    return !0;
                default:
                    return !1
                }
            }
            ,
            c.concat = function(e, t) {
                if (!i(e))
                    throw new TypeError('"list" argument must be an Array of Buffers');
                if (0 === e.length)
                    return c.alloc(0);
                var n;
                if (void 0 === t)
                    for (t = 0,
                    n = 0; n < e.length; ++n)
                        t += e[n].length;
                var r = c.allocUnsafe(t)
                  , o = 0;
                for (n = 0; n < e.length; ++n) {
                    var a = e[n];
                    if (!c.isBuffer(a))
                        throw new TypeError('"list" argument must be an Array of Buffers');
                    a.copy(r, o),
                    o += a.length
                }
                return r
            }
            ,
            c.byteLength = _,
            c.prototype._isBuffer = !0,
            c.prototype.swap16 = function() {
                var e = this.length;
                if (e % 2 !== 0)
                    throw new RangeError("Buffer size must be a multiple of 16-bits");
                for (var t = 0; t < e; t += 2)
                    w(this, t, t + 1);
                return this
            }
            ,
            c.prototype.swap32 = function() {
                var e = this.length;
                if (e % 4 !== 0)
                    throw new RangeError("Buffer size must be a multiple of 32-bits");
                for (var t = 0; t < e; t += 4)
                    w(this, t, t + 3),
                    w(this, t + 1, t + 2);
                return this
            }
            ,
            c.prototype.swap64 = function() {
                var e = this.length;
                if (e % 8 !== 0)
                    throw new RangeError("Buffer size must be a multiple of 64-bits");
                for (var t = 0; t < e; t += 8)
                    w(this, t, t + 7),
                    w(this, t + 1, t + 6),
                    w(this, t + 2, t + 5),
                    w(this, t + 3, t + 4);
                return this
            }
            ,
            c.prototype.toString = function() {
                var e = 0 | this.length;
                return 0 === e ? "" : 0 === arguments.length ? N(this, 0, e) : k.apply(this, arguments)
            }
            ,
            c.prototype.equals = function(e) {
                if (!c.isBuffer(e))
                    throw new TypeError("Argument must be a Buffer");
                return this === e || 0 === c.compare(this, e)
            }
            ,
            c.prototype.inspect = function() {
                var e = ""
                  , n = t.INSPECT_MAX_BYTES;
                return this.length > 0 && (e = this.toString("hex", 0, n).match(/.{2}/g).join(" "),
                this.length > n && (e += " ... ")),
                "<Buffer " + e + ">"
            }
            ,
            c.prototype.compare = function(e, t, n, r, o) {
                if (!c.isBuffer(e))
                    throw new TypeError("Argument must be a Buffer");
                if (void 0 === t && (t = 0),
                void 0 === n && (n = e ? e.length : 0),
                void 0 === r && (r = 0),
                void 0 === o && (o = this.length),
                t < 0 || n > e.length || r < 0 || o > this.length)
                    throw new RangeError("out of range index");
                if (r >= o && t >= n)
                    return 0;
                if (r >= o)
                    return -1;
                if (t >= n)
                    return 1;
                if (t >>>= 0,
                n >>>= 0,
                r >>>= 0,
                o >>>= 0,
                this === e)
                    return 0;
                for (var i = o - r, a = n - t, s = Math.min(i, a), u = this.slice(r, o), l = e.slice(t, n), f = 0; f < s; ++f)
                    if (u[f] !== l[f]) {
                        i = u[f],
                        a = l[f];
                        break
                    }
                return i < a ? -1 : a < i ? 1 : 0
            }
            ,
            c.prototype.includes = function(e, t, n) {
                return -1 !== this.indexOf(e, t, n)
            }
            ,
            c.prototype.indexOf = function(e, t, n) {
                return E(this, e, t, n, !0)
            }
            ,
            c.prototype.lastIndexOf = function(e, t, n) {
                return E(this, e, t, n, !1)
            }
            ,
            c.prototype.write = function(e, t, n, r) {
                if (void 0 === t)
                    r = "utf8",
                    n = this.length,
                    t = 0;
                else if (void 0 === n && "string" === typeof t)
                    r = t,
                    n = this.length,
                    t = 0;
                else {
                    if (!isFinite(t))
                        throw new Error("Buffer.write(string, encoding, offset[, length]) is no longer supported");
                    t |= 0,
                    isFinite(n) ? (n |= 0,
                    void 0 === r && (r = "utf8")) : (r = n,
                    n = void 0)
                }
                var o = this.length - t;
                if ((void 0 === n || n > o) && (n = o),
                e.length > 0 && (n < 0 || t < 0) || t > this.length)
                    throw new RangeError("Attempt to write outside buffer bounds");
                r || (r = "utf8");
                for (var i = !1; ; )
                    switch (r) {
                    case "hex":
                        return C(this, e, t, n);
                    case "utf8":
                    case "utf-8":
                        return T(this, e, t, n);
                    case "ascii":
                        return S(this, e, t, n);
                    case "latin1":
                    case "binary":
                        return I(this, e, t, n);
                    case "base64":
                        return O(this, e, t, n);
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return A(this, e, t, n);
                    default:
                        if (i)
                            throw new TypeError("Unknown encoding: " + r);
                        r = ("" + r).toLowerCase(),
                        i = !0
                    }
            }
            ,
            c.prototype.toJSON = function() {
                return {
                    type: "Buffer",
                    data: Array.prototype.slice.call(this._arr || this, 0)
                }
            }
            ;
            var D = 4096;
            function R(e) {
                var t = e.length;
                if (t <= D)
                    return String.fromCharCode.apply(String, e);
                var n = ""
                  , r = 0;
                while (r < t)
                    n += String.fromCharCode.apply(String, e.slice(r, r += D));
                return n
            }
            function P(e, t, n) {
                var r = "";
                n = Math.min(e.length, n);
                for (var o = t; o < n; ++o)
                    r += String.fromCharCode(127 & e[o]);
                return r
            }
            function L(e, t, n) {
                var r = "";
                n = Math.min(e.length, n);
                for (var o = t; o < n; ++o)
                    r += String.fromCharCode(e[o]);
                return r
            }
            function U(e, t, n) {
                var r = e.length;
                (!t || t < 0) && (t = 0),
                (!n || n < 0 || n > r) && (n = r);
                for (var o = "", i = t; i < n; ++i)
                    o += Y(e[i]);
                return o
            }
            function F(e, t, n) {
                for (var r = e.slice(t, n), o = "", i = 0; i < r.length; i += 2)
                    o += String.fromCharCode(r[i] + 256 * r[i + 1]);
                return o
            }
            function G(e, t, n) {
                if (e % 1 !== 0 || e < 0)
                    throw new RangeError("offset is not uint");
                if (e + t > n)
                    throw new RangeError("Trying to access beyond buffer length")
            }
            function j(e, t, n, r, o, i) {
                if (!c.isBuffer(e))
                    throw new TypeError('"buffer" argument must be a Buffer instance');
                if (t > o || t < i)
                    throw new RangeError('"value" argument is out of bounds');
                if (n + r > e.length)
                    throw new RangeError("Index out of range")
            }
            function q(e, t, n, r) {
                t < 0 && (t = 65535 + t + 1);
                for (var o = 0, i = Math.min(e.length - n, 2); o < i; ++o)
                    e[n + o] = (t & 255 << 8 * (r ? o : 1 - o)) >>> 8 * (r ? o : 1 - o)
            }
            function Z(e, t, n, r) {
                t < 0 && (t = 4294967295 + t + 1);
                for (var o = 0, i = Math.min(e.length - n, 4); o < i; ++o)
                    e[n + o] = t >>> 8 * (r ? o : 3 - o) & 255
            }
            function B(e, t, n, r, o, i) {
                if (n + r > e.length)
                    throw new RangeError("Index out of range");
                if (n < 0)
                    throw new RangeError("Index out of range")
            }
            function V(e, t, n, r, i) {
                return i || B(e, t, n, 4, 34028234663852886e22, -34028234663852886e22),
                o.write(e, t, n, r, 23, 4),
                n + 4
            }
            function H(e, t, n, r, i) {
                return i || B(e, t, n, 8, 17976931348623157e292, -17976931348623157e292),
                o.write(e, t, n, r, 52, 8),
                n + 8
            }
            c.prototype.slice = function(e, t) {
                var n, r = this.length;
                if (e = ~~e,
                t = void 0 === t ? r : ~~t,
                e < 0 ? (e += r,
                e < 0 && (e = 0)) : e > r && (e = r),
                t < 0 ? (t += r,
                t < 0 && (t = 0)) : t > r && (t = r),
                t < e && (t = e),
                c.TYPED_ARRAY_SUPPORT)
                    n = this.subarray(e, t),
                    n.__proto__ = c.prototype;
                else {
                    var o = t - e;
                    n = new c(o,void 0);
                    for (var i = 0; i < o; ++i)
                        n[i] = this[i + e]
                }
                return n
            }
            ,
            c.prototype.readUIntLE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || G(e, t, this.length);
                var r = this[e]
                  , o = 1
                  , i = 0;
                while (++i < t && (o *= 256))
                    r += this[e + i] * o;
                return r
            }
            ,
            c.prototype.readUIntBE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || G(e, t, this.length);
                var r = this[e + --t]
                  , o = 1;
                while (t > 0 && (o *= 256))
                    r += this[e + --t] * o;
                return r
            }
            ,
            c.prototype.readUInt8 = function(e, t) {
                return t || G(e, 1, this.length),
                this[e]
            }
            ,
            c.prototype.readUInt16LE = function(e, t) {
                return t || G(e, 2, this.length),
                this[e] | this[e + 1] << 8
            }
            ,
            c.prototype.readUInt16BE = function(e, t) {
                return t || G(e, 2, this.length),
                this[e] << 8 | this[e + 1]
            }
            ,
            c.prototype.readUInt32LE = function(e, t) {
                return t || G(e, 4, this.length),
                (this[e] | this[e + 1] << 8 | this[e + 2] << 16) + 16777216 * this[e + 3]
            }
            ,
            c.prototype.readUInt32BE = function(e, t) {
                return t || G(e, 4, this.length),
                16777216 * this[e] + (this[e + 1] << 16 | this[e + 2] << 8 | this[e + 3])
            }
            ,
            c.prototype.readIntLE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || G(e, t, this.length);
                var r = this[e]
                  , o = 1
                  , i = 0;
                while (++i < t && (o *= 256))
                    r += this[e + i] * o;
                return o *= 128,
                r >= o && (r -= Math.pow(2, 8 * t)),
                r
            }
            ,
            c.prototype.readIntBE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || G(e, t, this.length);
                var r = t
                  , o = 1
                  , i = this[e + --r];
                while (r > 0 && (o *= 256))
                    i += this[e + --r] * o;
                return o *= 128,
                i >= o && (i -= Math.pow(2, 8 * t)),
                i
            }
            ,
            c.prototype.readInt8 = function(e, t) {
                return t || G(e, 1, this.length),
                128 & this[e] ? -1 * (255 - this[e] + 1) : this[e]
            }
            ,
            c.prototype.readInt16LE = function(e, t) {
                t || G(e, 2, this.length);
                var n = this[e] | this[e + 1] << 8;
                return 32768 & n ? 4294901760 | n : n
            }
            ,
            c.prototype.readInt16BE = function(e, t) {
                t || G(e, 2, this.length);
                var n = this[e + 1] | this[e] << 8;
                return 32768 & n ? 4294901760 | n : n
            }
            ,
            c.prototype.readInt32LE = function(e, t) {
                return t || G(e, 4, this.length),
                this[e] | this[e + 1] << 8 | this[e + 2] << 16 | this[e + 3] << 24
            }
            ,
            c.prototype.readInt32BE = function(e, t) {
                return t || G(e, 4, this.length),
                this[e] << 24 | this[e + 1] << 16 | this[e + 2] << 8 | this[e + 3]
            }
            ,
            c.prototype.readFloatLE = function(e, t) {
                return t || G(e, 4, this.length),
                o.read(this, e, !0, 23, 4)
            }
            ,
            c.prototype.readFloatBE = function(e, t) {
                return t || G(e, 4, this.length),
                o.read(this, e, !1, 23, 4)
            }
            ,
            c.prototype.readDoubleLE = function(e, t) {
                return t || G(e, 8, this.length),
                o.read(this, e, !0, 52, 8)
            }
            ,
            c.prototype.readDoubleBE = function(e, t) {
                return t || G(e, 8, this.length),
                o.read(this, e, !1, 52, 8)
            }
            ,
            c.prototype.writeUIntLE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                n |= 0,
                !r) {
                    var o = Math.pow(2, 8 * n) - 1;
                    j(this, e, t, n, o, 0)
                }
                var i = 1
                  , a = 0;
                this[t] = 255 & e;
                while (++a < n && (i *= 256))
                    this[t + a] = e / i & 255;
                return t + n
            }
            ,
            c.prototype.writeUIntBE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                n |= 0,
                !r) {
                    var o = Math.pow(2, 8 * n) - 1;
                    j(this, e, t, n, o, 0)
                }
                var i = n - 1
                  , a = 1;
                this[t + i] = 255 & e;
                while (--i >= 0 && (a *= 256))
                    this[t + i] = e / a & 255;
                return t + n
            }
            ,
            c.prototype.writeUInt8 = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 1, 255, 0),
                c.TYPED_ARRAY_SUPPORT || (e = Math.floor(e)),
                this[t] = 255 & e,
                t + 1
            }
            ,
            c.prototype.writeUInt16LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 2, 65535, 0),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8) : q(this, e, t, !0),
                t + 2
            }
            ,
            c.prototype.writeUInt16BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 2, 65535, 0),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 8,
                this[t + 1] = 255 & e) : q(this, e, t, !1),
                t + 2
            }
            ,
            c.prototype.writeUInt32LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 4, 4294967295, 0),
                c.TYPED_ARRAY_SUPPORT ? (this[t + 3] = e >>> 24,
                this[t + 2] = e >>> 16,
                this[t + 1] = e >>> 8,
                this[t] = 255 & e) : Z(this, e, t, !0),
                t + 4
            }
            ,
            c.prototype.writeUInt32BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 4, 4294967295, 0),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 24,
                this[t + 1] = e >>> 16,
                this[t + 2] = e >>> 8,
                this[t + 3] = 255 & e) : Z(this, e, t, !1),
                t + 4
            }
            ,
            c.prototype.writeIntLE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                !r) {
                    var o = Math.pow(2, 8 * n - 1);
                    j(this, e, t, n, o - 1, -o)
                }
                var i = 0
                  , a = 1
                  , s = 0;
                this[t] = 255 & e;
                while (++i < n && (a *= 256))
                    e < 0 && 0 === s && 0 !== this[t + i - 1] && (s = 1),
                    this[t + i] = (e / a >> 0) - s & 255;
                return t + n
            }
            ,
            c.prototype.writeIntBE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                !r) {
                    var o = Math.pow(2, 8 * n - 1);
                    j(this, e, t, n, o - 1, -o)
                }
                var i = n - 1
                  , a = 1
                  , s = 0;
                this[t + i] = 255 & e;
                while (--i >= 0 && (a *= 256))
                    e < 0 && 0 === s && 0 !== this[t + i + 1] && (s = 1),
                    this[t + i] = (e / a >> 0) - s & 255;
                return t + n
            }
            ,
            c.prototype.writeInt8 = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 1, 127, -128),
                c.TYPED_ARRAY_SUPPORT || (e = Math.floor(e)),
                e < 0 && (e = 255 + e + 1),
                this[t] = 255 & e,
                t + 1
            }
            ,
            c.prototype.writeInt16LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 2, 32767, -32768),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8) : q(this, e, t, !0),
                t + 2
            }
            ,
            c.prototype.writeInt16BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 2, 32767, -32768),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 8,
                this[t + 1] = 255 & e) : q(this, e, t, !1),
                t + 2
            }
            ,
            c.prototype.writeInt32LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 4, 2147483647, -2147483648),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8,
                this[t + 2] = e >>> 16,
                this[t + 3] = e >>> 24) : Z(this, e, t, !0),
                t + 4
            }
            ,
            c.prototype.writeInt32BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || j(this, e, t, 4, 2147483647, -2147483648),
                e < 0 && (e = 4294967295 + e + 1),
                c.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 24,
                this[t + 1] = e >>> 16,
                this[t + 2] = e >>> 8,
                this[t + 3] = 255 & e) : Z(this, e, t, !1),
                t + 4
            }
            ,
            c.prototype.writeFloatLE = function(e, t, n) {
                return V(this, e, t, !0, n)
            }
            ,
            c.prototype.writeFloatBE = function(e, t, n) {
                return V(this, e, t, !1, n)
            }
            ,
            c.prototype.writeDoubleLE = function(e, t, n) {
                return H(this, e, t, !0, n)
            }
            ,
            c.prototype.writeDoubleBE = function(e, t, n) {
                return H(this, e, t, !1, n)
            }
            ,
            c.prototype.copy = function(e, t, n, r) {
                if (n || (n = 0),
                r || 0 === r || (r = this.length),
                t >= e.length && (t = e.length),
                t || (t = 0),
                r > 0 && r < n && (r = n),
                r === n)
                    return 0;
                if (0 === e.length || 0 === this.length)
                    return 0;
                if (t < 0)
                    throw new RangeError("targetStart out of bounds");
                if (n < 0 || n >= this.length)
                    throw new RangeError("sourceStart out of bounds");
                if (r < 0)
                    throw new RangeError("sourceEnd out of bounds");
                r > this.length && (r = this.length),
                e.length - t < r - n && (r = e.length - t + n);
                var o, i = r - n;
                if (this === e && n < t && t < r)
                    for (o = i - 1; o >= 0; --o)
                        e[o + t] = this[o + n];
                else if (i < 1e3 || !c.TYPED_ARRAY_SUPPORT)
                    for (o = 0; o < i; ++o)
                        e[o + t] = this[o + n];
                else
                    Uint8Array.prototype.set.call(e, this.subarray(n, n + i), t);
                return i
            }
            ,
            c.prototype.fill = function(e, t, n, r) {
                if ("string" === typeof e) {
                    if ("string" === typeof t ? (r = t,
                    t = 0,
                    n = this.length) : "string" === typeof n && (r = n,
                    n = this.length),
                    1 === e.length) {
                        var o = e.charCodeAt(0);
                        o < 256 && (e = o)
                    }
                    if (void 0 !== r && "string" !== typeof r)
                        throw new TypeError("encoding must be a string");
                    if ("string" === typeof r && !c.isEncoding(r))
                        throw new TypeError("Unknown encoding: " + r)
                } else
                    "number" === typeof e && (e &= 255);
                if (t < 0 || this.length < t || this.length < n)
                    throw new RangeError("Out of range index");
                if (n <= t)
                    return this;
                var i;
                if (t >>>= 0,
                n = void 0 === n ? this.length : n >>> 0,
                e || (e = 0),
                "number" === typeof e)
                    for (i = t; i < n; ++i)
                        this[i] = e;
                else {
                    var a = c.isBuffer(e) ? e : $(new c(e,r).toString())
                      , s = a.length;
                    for (i = 0; i < n - t; ++i)
                        this[i + t] = a[i % s]
                }
                return this
            }
            ;
            var W = /[^+\/0-9A-Za-z-_]/g;
            function z(e) {
                if (e = K(e).replace(W, ""),
                e.length < 2)
                    return "";
                while (e.length % 4 !== 0)
                    e += "=";
                return e
            }
            function K(e) {
                return e.trim ? e.trim() : e.replace(/^\s+|\s+$/g, "")
            }
            function Y(e) {
                return e < 16 ? "0" + e.toString(16) : e.toString(16)
            }
            function $(e, t) {
                var n;
                t = t || 1 / 0;
                for (var r = e.length, o = null, i = [], a = 0; a < r; ++a) {
                    if (n = e.charCodeAt(a),
                    n > 55295 && n < 57344) {
                        if (!o) {
                            if (n > 56319) {
                                (t -= 3) > -1 && i.push(239, 191, 189);
                                continue
                            }
                            if (a + 1 === r) {
                                (t -= 3) > -1 && i.push(239, 191, 189);
                                continue
                            }
                            o = n;
                            continue
                        }
                        if (n < 56320) {
                            (t -= 3) > -1 && i.push(239, 191, 189),
                            o = n;
                            continue
                        }
                        n = 65536 + (o - 55296 << 10 | n - 56320)
                    } else
                        o && (t -= 3) > -1 && i.push(239, 191, 189);
                    if (o = null,
                    n < 128) {
                        if ((t -= 1) < 0)
                            break;
                        i.push(n)
                    } else if (n < 2048) {
                        if ((t -= 2) < 0)
                            break;
                        i.push(n >> 6 | 192, 63 & n | 128)
                    } else if (n < 65536) {
                        if ((t -= 3) < 0)
                            break;
                        i.push(n >> 12 | 224, n >> 6 & 63 | 128, 63 & n | 128)
                    } else {
                        if (!(n < 1114112))
                            throw new Error("Invalid code point");
                        if ((t -= 4) < 0)
                            break;
                        i.push(n >> 18 | 240, n >> 12 & 63 | 128, n >> 6 & 63 | 128, 63 & n | 128)
                    }
                }
                return i
            }
            function X(e) {
                for (var t = [], n = 0; n < e.length; ++n)
                    t.push(255 & e.charCodeAt(n));
                return t
            }
            function J(e, t) {
                for (var n, r, o, i = [], a = 0; a < e.length; ++a) {
                    if ((t -= 2) < 0)
                        break;
                    n = e.charCodeAt(a),
                    r = n >> 8,
                    o = n % 256,
                    i.push(o),
                    i.push(r)
                }
                return i
            }
            function Q(e) {
                return r.toByteArray(z(e))
            }
            function ee(e, t, n, r) {
                for (var o = 0; o < r; ++o) {
                    if (o + n >= t.length || o >= e.length)
                        break;
                    t[o + n] = e[o]
                }
                return o
            }
            function te(e) {
                return e !== e
            }
        },
        87300: function(e) {
            var t = {}.toString;
            e.exports = Array.isArray || function(e) {
                return "[object Array]" == t.call(e)
            }
        },
           79742: function(e, t) {
            "use strict";
            t.byteLength = c,
            t.toByteArray = f,
            t.fromByteArray = h;
            for (var n = [], r = [], o = "undefined" !== typeof Uint8Array ? Uint8Array : Array, i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", a = 0, s = i.length; a < s; ++a)
                n[a] = i[a],
                r[i.charCodeAt(a)] = a;
            function u(e) {
                var t = e.length;
                if (t % 4 > 0)
                    throw new Error("Invalid string. Length must be a multiple of 4");
                var n = e.indexOf("=");
                -1 === n && (n = t);
                var r = n === t ? 0 : 4 - n % 4;
                return [n, r]
            }
            function c(e) {
                var t = u(e)
                  , n = t[0]
                  , r = t[1];
                return 3 * (n + r) / 4 - r
            }
            function l(e, t, n) {
                return 3 * (t + n) / 4 - n
            }
            function f(e) {
                var t, n, i = u(e), a = i[0], s = i[1], c = new o(l(e, a, s)), f = 0, d = s > 0 ? a - 4 : a;
                for (n = 0; n < d; n += 4)
                    t = r[e.charCodeAt(n)] << 18 | r[e.charCodeAt(n + 1)] << 12 | r[e.charCodeAt(n + 2)] << 6 | r[e.charCodeAt(n + 3)],
                    c[f++] = t >> 16 & 255,
                    c[f++] = t >> 8 & 255,
                    c[f++] = 255 & t;
                return 2 === s && (t = r[e.charCodeAt(n)] << 2 | r[e.charCodeAt(n + 1)] >> 4,
                c[f++] = 255 & t),
                1 === s && (t = r[e.charCodeAt(n)] << 10 | r[e.charCodeAt(n + 1)] << 4 | r[e.charCodeAt(n + 2)] >> 2,
                c[f++] = t >> 8 & 255,
                c[f++] = 255 & t),
                c
            }
            function d(e) {
                return n[e >> 18 & 63] + n[e >> 12 & 63] + n[e >> 6 & 63] + n[63 & e]
            }
            function p(e, t, n) {
                for (var r, o = [], i = t; i < n; i += 3)
                    r = (e[i] << 16 & 16711680) + (e[i + 1] << 8 & 65280) + (255 & e[i + 2]),
                    o.push(d(r));
                return o.join("")
            }
            function h(e) {
                for (var t, r = e.length, o = r % 3, i = [], a = 16383, s = 0, u = r - o; s < u; s += a)
                    i.push(p(e, s, s + a > u ? u : s + a));
                return 1 === o ? (t = e[r - 1],
                i.push(n[t >> 2] + n[t << 4 & 63] + "==")) : 2 === o && (t = (e[r - 2] << 8) + e[r - 1],
                i.push(n[t >> 10] + n[t >> 4 & 63] + n[t << 2 & 63] + "=")),
                i.join("")
            }
            r["-".charCodeAt(0)] = 62,
            r["_".charCodeAt(0)] = 63
        },
         80645: function(e, t) {
            t.read = function(e, t, n, r, o) {
                var i, a, s = 8 * o - r - 1, u = (1 << s) - 1, c = u >> 1, l = -7, f = n ? o - 1 : 0, d = n ? -1 : 1, p = e[t + f];
                for (f += d,
                i = p & (1 << -l) - 1,
                p >>= -l,
                l += s; l > 0; i = 256 * i + e[t + f],
                f += d,
                l -= 8)
                    ;
                for (a = i & (1 << -l) - 1,
                i >>= -l,
                l += r; l > 0; a = 256 * a + e[t + f],
                f += d,
                l -= 8)
                    ;
                if (0 === i)
                    i = 1 - c;
                else {
                    if (i === u)
                        return a ? NaN : 1 / 0 * (p ? -1 : 1);
                    a += Math.pow(2, r),
                    i -= c
                }
                return (p ? -1 : 1) * a * Math.pow(2, i - r)
            }
            ,
            t.write = function(e, t, n, r, o, i) {
                var a, s, u, c = 8 * i - o - 1, l = (1 << c) - 1, f = l >> 1, d = 23 === o ? Math.pow(2, -24) - Math.pow(2, -77) : 0, p = r ? 0 : i - 1, h = r ? 1 : -1, v = t < 0 || 0 === t && 1 / t < 0 ? 1 : 0;
                for (t = Math.abs(t),
                isNaN(t) || t === 1 / 0 ? (s = isNaN(t) ? 1 : 0,
                a = l) : (a = Math.floor(Math.log(t) / Math.LN2),
                t * (u = Math.pow(2, -a)) < 1 && (a--,
                u *= 2),
                t += a + f >= 1 ? d / u : d * Math.pow(2, 1 - f),
                t * u >= 2 && (a++,
                u /= 2),
                a + f >= l ? (s = 0,
                a = l) : a + f >= 1 ? (s = (t * u - 1) * Math.pow(2, o),
                a += f) : (s = t * Math.pow(2, f - 1) * Math.pow(2, o),
                a = 0)); o >= 8; e[n + p] = 255 & s,
                p += h,
                s /= 256,
                o -= 8)
                    ;
                for (a = a << o | s,
                c += o; c > 0; e[n + p] = 255 & a,
                p += h,
                a /= 256,
                c -= 8)
                    ;
                e[n + p - h] |= 128 * v
            }
        },
    }
      , t = {};
    function n(r) {
        console.log('r:::',r)
        var o = t[r];
        if (void 0 !== o)
            return o.exports;
        var i = t[r] = {
            id: r,
            loaded: !1,
            exports: {}
        };
        return e[r].call(i.exports, i, i.exports, n),
        i.loaded = !0,
        i.exports
    }
    window.loader = n
    n.m = e,
    function() {
        n.amdO = {}
    }(),
    function() {
        n.n = function(e) {
            var t = e && e.__esModule ? function() {
                return e["default"]
            }
            : function() {
                return e
            }
            ;
            return n.d(t, {
                a: t
            }),
            t
        }
    }(),
    function() {
        var e, t = Object.getPrototypeOf ? function(e) {
            return Object.getPrototypeOf(e)
        }
        : function(e) {
            return e.__proto__
        }
        ;
        n.t = function(r, o) {
            if (1 & o && (r = this(r)),
            8 & o)
                return r;
            if ("object" === typeof r && r) {
                if (4 & o && r.__esModule)
                    return r;
                if (16 & o && "function" === typeof r.then)
                    return r
            }
            var i = Object.create(null);
            n.r(i);
            var a = {};
            e = e || [null, t({}), t([]), t(t)];
            for (var s = 2 & o && r; "object" == typeof s && !~e.indexOf(s); s = t(s))
                Object.getOwnPropertyNames(s).forEach((function(e) {
                    a[e] = function() {
                        return r[e]
                    }
                }
                ));
            return a["default"] = function() {
                return r
            }
            ,
            n.d(i, a),
            i
        }
    }(),
    function() {
        n.d = function(e, t) {
            for (var r in t)
                n.o(t, r) && !n.o(e, r) && Object.defineProperty(e, r, {
                    enumerable: !0,
                    get: t[r]
                })
        }
    }(),
    function() {
        n.f = {},
        n.e = function(e) {
            return Promise.all(Object.keys(n.f).reduce((function(t, r) {
                return n.f[r](e, t),
                t
            }
            ), []))
        }
    }(),
    function() {
        n.u = function(e) {
            return ({
                68: "p__BoardManageLeaderboard",
                79: "p__IDxyer__containers__Threads",
                305: "p__Setting__containers__BlackList",
                611: "p__ImageUpload",
                868: "p__Setting",
                938: "p__Thread__index",
                1099: "p__AppDownload",
                1159: "p__myhome",
                1193: "p__IDxyer__Edit",
                1681: "p__IDxyer__containers__Scores",
                1717: "layouts__index",
                1833: "p__DingDang__containers__Record",
                1915: "p__DingDang",
                2845: "p__IDxyer__containers__Attachments",
                3371: "p__Home__index",
                3550: "p__Case__Home",
                3589: "p__NewPost__index",
                3732: "p__Roundtable__RoundtableDetail",
                3835: "p__DingDang__containers__Earn",
                4331: "p__Setting__containers__Message",
                4664: "p__Case__Introduce",
                5334: "p__Case__Search",
                5578: "p__IDxyer__containers__Replies",
                6003: "p__DingDang__containers__Lottery",
                6447: "p__IDxyer__containers__Followings",
                7045: "p__Setting__containers__Interest",
                7125: "p__Notification",
                7191: "p__IDxyer__containers__Specials",
                7551: "p__Setting__containers__Privacy",
                7819: "p__ModeratorWorkbench",
                8209: "p__IDxyer__containers__Collections",
                8554: "p__IDxyer__containers__Moments",
                8888: "p__IDxyer",
                8908: "p__Roundtable",
                8909: "p__Setting__containers__Account",
                9147: "p__Roundtable__RoundTableThread",
                9603: "p__Board__index",
                9747: "p__Case"
            }[e] || e) + ".async." + {
                61: "23d72b65",
                68: "cc3a43a4",
                79: "264c922f",
                142: "51503721",
                222: "0fdbb15d",
                305: "4ee9a5fe",
                327: "49f3fd6b",
                611: "a7fa3a46",
                816: "635b343d",
                843: "8236325e",
                868: "1ee47057",
                938: "cdd0f179",
                939: "d3244cd1",
                1032: "f39ae3cd",
                1099: "196099ce",
                1159: "9926f0cc",
                1193: "bd7a3ccf",
                1274: "50ce902b",
                1370: "bdd0e2c7",
                1681: "f97e3c4a",
                1717: "bea0553e",
                1833: "02e94dd4",
                1915: "ff26c2d8",
                1932: "9ecae30d",
                2038: "79ee400e",
                2145: "7ea3d74d",
                2162: "1c22a434",
                2205: "ded08767",
                2217: "680eeed7",
                2235: "72433785",
                2237: "1b48b2ce",
                2327: "2170b055",
                2845: "6d067935",
                2923: "e37311ac",
                3063: "581bc7d1",
                3371: "0ab811ea",
                3550: "b13f760d",
                3553: "6dbdc0e7",
                3586: "ee1344b8",
                3589: "cb7ea09f",
                3707: "23bc9720",
                3732: "a9b0cd06",
                3835: "71ea335d",
                4331: "a70acd4e",
                4526: "bbdd2d89",
                4643: "6f62ae6e",
                4664: "72b98ad1",
                4690: "c527a5f8",
                5049: "aaed3d97",
                5334: "3552ac61",
                5342: "ade5ca9f",
                5367: "1a8a9fff",
                5559: "3b35a90f",
                5565: "43a09eaa",
                5578: "e1255118",
                5606: "54c1b34d",
                5683: "0966280b",
                5912: "bbcaa9ac",
                5975: "87f93f5f",
                6003: "627f1751",
                6016: "99de049b",
                6246: "c99cb358",
                6278: "321559d8",
                6361: "479c82e6",
                6393: "e083f61e",
                6447: "61841e24",
                6694: "c5522615",
                6696: "183aca98",
                6866: "280e0ff6",
                6934: "0458154d",
                7002: "749eee93",
                7045: "4cbf5110",
                7125: "ecf2065c",
                7191: "4d41364a",
                7551: "2688b30e",
                7672: "b170c641",
                7722: "6bbb1e8c",
                7819: "6afa84ca",
                7890: "d1d004be",
                8209: "f2b7c0b5",
                8391: "260dfdce",
                8554: "8a926f0d",
                8607: "10074ecd",
                8826: "51fc36aa",
                8888: "b69f11ed",
                8908: "655d5c4a",
                8909: "88c4dd25",
                9105: "17d4dc8e",
                9147: "5457108e",
                9353: "714c988a",
                9361: "ecde7eb7",
                9600: "bea8a15d",
                9603: "155c27a9",
                9698: "a023a6a3",
                9747: "faf57ab8",
                9794: "be068cbd"
            }[e] + ".js"
        }
    }(),
    function() {
        n.miniCssF = function(e) {
            return 4620 === e ? "umi.bundle.css" : ({
                68: "p__BoardManageLeaderboard",
                79: "p__IDxyer__containers__Threads",
                305: "p__Setting__containers__BlackList",
                611: "p__ImageUpload",
                868: "p__Setting",
                938: "p__Thread__index",
                1099: "p__AppDownload",
                1159: "p__myhome",
                1193: "p__IDxyer__Edit",
                1681: "p__IDxyer__containers__Scores",
                1717: "layouts__index",
                1833: "p__DingDang__containers__Record",
                1915: "p__DingDang",
                2845: "p__IDxyer__containers__Attachments",
                3371: "p__Home__index",
                3550: "p__Case__Home",
                3589: "p__NewPost__index",
                3732: "p__Roundtable__RoundtableDetail",
                3835: "p__DingDang__containers__Earn",
                4331: "p__Setting__containers__Message",
                4664: "p__Case__Introduce",
                5334: "p__Case__Search",
                5578: "p__IDxyer__containers__Replies",
                6003: "p__DingDang__containers__Lottery",
                6447: "p__IDxyer__containers__Followings",
                7045: "p__Setting__containers__Interest",
                7125: "p__Notification",
                7191: "p__IDxyer__containers__Specials",
                7551: "p__Setting__containers__Privacy",
                7819: "p__ModeratorWorkbench",
                8209: "p__IDxyer__containers__Collections",
                8554: "p__IDxyer__containers__Moments",
                8888: "p__IDxyer",
                8908: "p__Roundtable",
                8909: "p__Setting__containers__Account",
                9147: "p__Roundtable__RoundTableThread",
                9603: "p__Board__index",
                9747: "p__Case"
            }[e] || e) + ".async." + {
                61: "d57a8f2a",
                68: "a6017a4f",
                79: "ea94b953",
                142: "31d6cfe0",
                222: "31d6cfe0",
                305: "a239cf6c",
                327: "31d6cfe0",
                611: "1b86095c",
                816: "31d6cfe0",
                843: "dde205ca",
                868: "62738ce5",
                938: "3bef397b",
                939: "31d6cfe0",
                1032: "31d6cfe0",
                1099: "5f1aaa38",
                1159: "31d6cfe0",
                1193: "19167ad5",
                1274: "31d6cfe0",
                1370: "336d9a58",
                1681: "2e8b72cb",
                1717: "d41ce995",
                1833: "2f551771",
                1915: "79c00a9a",
                1932: "31d6cfe0",
                2038: "8d4a679c",
                2145: "31d6cfe0",
                2162: "a644e42e",
                2205: "31d6cfe0",
                2217: "31d6cfe0",
                2235: "31d6cfe0",
                2237: "31d6cfe0",
                2327: "31d6cfe0",
                2845: "1122565f",
                2923: "31d6cfe0",
                3063: "31d6cfe0",
                3371: "34a2e849",
                3550: "499d5d55",
                3553: "31d6cfe0",
                3586: "4530724c",
                3589: "1bcdd702",
                3707: "31d6cfe0",
                3732: "5c4cb9f7",
                3835: "ae83d3dd",
                4331: "fe6929a5",
                4526: "31d6cfe0",
                4643: "31d6cfe0",
                4664: "b5d46035",
                4690: "9b21d809",
                5049: "31d6cfe0",
                5334: "b8fa008e",
                5342: "31d6cfe0",
                5367: "31d6cfe0",
                5559: "31d6cfe0",
                5565: "f631115a",
                5578: "2cc45596",
                5606: "31d6cfe0",
                5683: "31d6cfe0",
                5912: "31d6cfe0",
                5975: "31d6cfe0",
                6003: "dd06e89e",
                6016: "2eda635f",
                6246: "31d6cfe0",
                6278: "95e1297b",
                6361: "31d6cfe0",
                6393: "7c44bbfb",
                6447: "7b8470c4",
                6694: "31d6cfe0",
                6696: "31d6cfe0",
                6866: "31d6cfe0",
                6934: "31d6cfe0",
                7002: "31d6cfe0",
                7045: "48e18bd9",
                7125: "45b9718f",
                7191: "5ede94f1",
                7551: "a2cf27b1",
                7672: "31d6cfe0",
                7722: "31d6cfe0",
                7819: "3e24eef3",
                7890: "31d6cfe0",
                8209: "3f419768",
                8391: "31d6cfe0",
                8554: "57a4447f",
                8607: "31d6cfe0",
                8826: "31d6cfe0",
                8888: "72953c81",
                8908: "d304cd7c",
                8909: "6f500d91",
                9105: "31d6cfe0",
                9147: "db8789d8",
                9353: "31d6cfe0",
                9361: "31d6cfe0",
                9600: "31d6cfe0",
                9603: "081db5c1",
                9698: "fba560b8",
                9747: "5634f2c3",
                9794: "31d6cfe0"
            }[e] + ".css"
        }
    }(),
    function() {
        n.g = function() {
            if ("object" === typeof globalThis)
                return globalThis;
            try {
                return this || new Function("return this")()
            } catch (e) {
                if ("object" === typeof window)
                    return window
            }
        }()
    }(),
    function() {
        n.hmd = function(e) {
            return e = Object.create(e),
            e.children || (e.children = []),
            Object.defineProperty(e, "exports", {
                enumerable: !0,
                set: function() {
                    throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: " + e.id)
                }
            }),
            e
        }
    }(),
    function() {
        n.o = function(e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
    }(),
    function() {
        var e = {}
          , t = "bbs-pc:";
        n.l = function(r, o, i, a) {
            if (e[r])
                e[r].push(o);
            else {
                var s, u;
                if (void 0 !== i)
                    for (var c = document.getElementsByTagName("script"), l = 0; l < c.length; l++) {
                        var f = c[l];
                        if (f.getAttribute("src") == r || f.getAttribute("data-webpack") == t + i) {
                            s = f;
                            break
                        }
                    }
                s || (u = !0,
                s = document.createElement("script"),
                s.charset = "utf-8",
                s.timeout = 120,
                n.nc && s.setAttribute("nonce", n.nc),
                s.setAttribute("data-webpack", t + i),
                s.src = r),
                e[r] = [o];
                var d = function(t, n) {
                    s.onerror = s.onload = null,
                    clearTimeout(p);
                    var o = e[r];
                    if (delete e[r],
                    s.parentNode && s.parentNode.removeChild(s),
                    o && o.forEach((function(e) {
                        return e(n)
                    }
                    )),
                    t)
                        return t(n)
                }
                  , p = setTimeout(d.bind(null, void 0, {
                    type: "timeout",
                    target: s
                }), 12e4);
                s.onerror = d.bind(null, s.onerror),
                s.onload = d.bind(null, s.onload),
                u && document.head.appendChild(s)
            }
        }
    }(),
    function() {
        n.r = function(e) {
            "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
            Object.defineProperty(e, "__esModule", {
                value: !0
            })
        }
    }(),
    function() {
        n.nmd = function(e) {
            return e.paths = [],
            e.children || (e.children = []),
            e
        }
    }(),
    function() {
        n.p = "//a1.dxycdn.com/gitrepo/bbs-pc/dist/"
    }(),
    function() {
        var e = function(e, t, n) {
            var r = document.createElement("link");
            r.rel = "stylesheet",
            r.type = "text/css",
            r.onload = t,
            r.onerror = function(t) {
                var o = t && t.target && t.target.src || e
                  , i = new Error("Loading CSS chunk " + chunkId + " failed.\n(" + o + ")");
                i.code = "CSS_CHUNK_LOAD_FAILED",
                i.request = o,
                r.parentNode.removeChild(r),
                n(i)
            }
            ,
            r.href = e;
            var o = document.getElementsByTagName("head")[0];
            return o.appendChild(r),
            r
        }
          , t = function(e, t) {
            for (var n = document.getElementsByTagName("link"), r = 0; r < n.length; r++) {
                var o = n[r]
                  , i = o.getAttribute("data-href") || o.getAttribute("href");
                if ("stylesheet" === o.rel && (i === e || i === t))
                    return o
            }
            var a = document.getElementsByTagName("style");
            for (r = 0; r < a.length; r++) {
                o = a[r],
                i = o.getAttribute("data-href");
                if (i === e || i === t)
                    return o
            }
        }
          , r = function(r) {
            return new Promise((function(o, i) {
                var a = n.miniCssF(r)
                  , s = n.p + a;
                if (t(a, s))
                    return o();
                e(s, o, i)
            }
            ))
        }
          , o = {
            4620: 0
        };
        n.f.miniCss = function(e, t) {
            var n = {
                61: 1,
                68: 1,
                79: 1,
                305: 1,
                611: 1,
                843: 1,
                868: 1,
                938: 1,
                1099: 1,
                1193: 1,
                1370: 1,
                1681: 1,
                1717: 1,
                1833: 1,
                1915: 1,
                2038: 1,
                2162: 1,
                2845: 1,
                3371: 1,
                3550: 1,
                3586: 1,
                3589: 1,
                3732: 1,
                3835: 1,
                4331: 1,
                4664: 1,
                4690: 1,
                5334: 1,
                5565: 1,
                5578: 1,
                6003: 1,
                6016: 1,
                6278: 1,
                6393: 1,
                6447: 1,
                7045: 1,
                7125: 1,
                7191: 1,
                7551: 1,
                7819: 1,
                8209: 1,
                8554: 1,
                8888: 1,
                8908: 1,
                8909: 1,
                9147: 1,
                9603: 1,
                9698: 1,
                9747: 1
            };
            o[e] ? t.push(o[e]) : 0 !== o[e] && n[e] && t.push(o[e] = r(e).then((function() {
                o[e] = 0
            }
            ), (function(t) {
                throw delete o[e],
                t
            }
            )))
        }
    }(),
    function() {
        var e = {
            4620: 0
        };
        n.f.j = function(t, r) {
            var o = n.o(e, t) ? e[t] : void 0;
            if (0 !== o)
                if (o)
                    r.push(o[2]);
                else {
                    var i = new Promise((function(n, r) {
                        o = e[t] = [n, r]
                    }
                    ));
                    r.push(o[2] = i);
                    var a = n.p + n.u(t)
                      , s = new Error
                      , u = function(r) {
                        if (n.o(e, t) && (o = e[t],
                        0 !== o && (e[t] = void 0),
                        o)) {
                            var i = r && ("load" === r.type ? "missing" : r.type)
                              , a = r && r.target && r.target.src;
                            s.message = "Loading chunk " + t + " failed.\n(" + i + ": " + a + ")",
                            s.name = "ChunkLoadError",
                            s.type = i,
                            s.request = a,
                            o[1](s)
                        }
                    };
                    n.l(a, u, "chunk-" + t, t)
                }
        }
        ;
        var t = function(t, r) {
            var o, i, a = r[0], s = r[1], u = r[2], c = 0;
            for (o in s)
                n.o(s, o) && (n.m[o] = s[o]);
            if (u)
                u(n);
            for (t && t(r); c < a.length; c++)
                i = a[c],
                n.o(e, i) && e[i] && e[i][0](),
                e[a[c]] = 0
        }
          , r = [];
        r.forEach(t.bind(null, 0)),
        r.push = t.bind(null, r.push.bind(r))
    }();
    
    n(88086)
}
)();
function get_data(){
    return window.f()
}

console.log(window.f())