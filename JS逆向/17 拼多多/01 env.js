window = global;

delete global;
delete Buffer;

document = {
    addEventListener: function () {
    },
    cookie: '_nano_fp=XpmonpCql0Xqn5XJno_Ut7MFFzjHDdTjr3Ho7S6a'

}
screen = {
    availWidth: 1728,
    availHeight: 1085,
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    webdriver: false,
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

history = {}
history.back = function () {
}

location = {
    hash: "",
    host: "www.pinduoduo.com",
    hostname: "www.pinduoduo.com",
    href: "https://www.pinduoduo.com/home/baby/",
    origin: "https://www.pinduoduo.com",
    pathname: "/home/baby/",
    port: "",
    protocol: "https:",
}


/*function browser_proxy(obj) {

    return new Proxy(obj, {
        get: function (target, property, receiver) {
            //debugger;
            console.log("get: ", obj, property,target[property]);
            return target[property];
        },
        set: function (target, property, value) {
            //debugger;
            console.log("set: ", obj, property);
            return Reflect.set(...arguments);
        },
    })
}

window = browser_proxy(window);
document = browser_proxy(document);
navigator = browser_proxy(navigator);
screen = browser_proxy(screen);
history = browser_proxy(history);
location = browser_proxy(location);*/
