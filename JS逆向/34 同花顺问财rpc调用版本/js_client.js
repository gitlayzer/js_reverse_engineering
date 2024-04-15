// 需要浏览器执行，前提是已经将获取值的方法赋值给了window全局对象
(function () {
    // 浏览器逻辑:
    let ws = new WebSocket("ws://127.0.0.1:8888/register.ws?name=iwencai");

    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function (msg) {

        console.log("msg:::", msg.data);
        let ret = window.xxx(); // 你得找到加密入口...
        console.log("计算完毕, 结果是", ret);
        // 返回结果
        ws.send(ret);
    }
})();
