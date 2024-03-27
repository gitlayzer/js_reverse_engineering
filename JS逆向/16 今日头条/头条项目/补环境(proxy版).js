

function my_proxy(obj) {
    return new Proxy(obj, {
        get(target, p, receiver) {
            debugger;
            let val = Reflect.get(...arguments);
            console.log("get操作", target, ":::获取属性>", p, ":::值>", val);
            return val;
        },
        set(target, p, value, receiver) {
            debugger;
            console.log("set操作", target, ":::设置属性>", p, ":::值>", value);
            return Reflect.set(...arguments);
        }
    });
}

`先将几个通用的 对象补全`

debugger;
window = {}
window = this;
Window = function Window() {
};
Object.setPrototypeOf(window, Window.prototype);


document = {
    referrer: 'https://www.baidu.com/link?url=0yoJdbvhxZp-OpF_lH5XrS6v9M6WKlT7Ia-CSe71_K48GjXa0x78wsXyBgXyOU-0&wd=&eqid=e81dffcc00014af2000000046603a2ad'

}
Document = function (){

}

Object.setPrototypeOf(document,Document.prototype)

location = {
    href : 'https://www.toutiao.com/',
    protocol : 'https'
}

Location = function Location(){

}
Object.setPrototypeOf(location,Location.prototype)


navigator = {
    userAgent : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
Navigator = function Navigator(){

}
Object.setPrototypeOf(navigator,Navigator.prototype)

debugger;
window = my_proxy(window)
document = my_proxy(document)
location = my_proxy(location)
navigator = my_proxy(navigator)