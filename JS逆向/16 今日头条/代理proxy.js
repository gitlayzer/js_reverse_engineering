// 可以监听对象下所有的属性操作
var window = {
    username: "yuan",
    age: 22
}

// 传入对象,用于监听此对象下 方法或者属性操作
window = new Proxy(window, {
    get(target, p, receiver) {
        debugger;
        console.log("target: ", target);
        console.log("p: ", p);
        // return window['username'];/// 这里如果这样写. 有递归风险的...
        // return Reflect.get(...arguments);
        return Reflect.get(target, p);
    },
    set(target, p, value, receiver) {
        debugger;
        console.log("设置操作")
        Reflect.set(target, p, value);
    }
});

console.log(window.username);
console.log(window.age);
window.username = "rain"
window.age = 18

// 打赏debugger 可以通过node-inspect 来浏览器操作  node-inspect 代理proxy.js
