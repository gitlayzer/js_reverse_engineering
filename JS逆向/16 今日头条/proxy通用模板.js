function my_proxy(obj) {
    return new Proxy(obj, {
        get(target, p, receiver) {
            let val = Reflect.get(...arguments);
            console.log("get操作", target, ":::获取属性>", p, ":::值>", val);
            return val;
        },
        set(target, p, value, receiver) {
            console.log("set操作", target, ":::设置属性>", p, ":::值>", value);
            return Reflect.set(...arguments);
        }
    });
}

`
使用方法

obj = my_proxy(obj)
`