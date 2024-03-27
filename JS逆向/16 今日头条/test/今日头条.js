var vm = require("vm2")
var fs = require("fs") // nodejs内置的读取文件的写法
const {VM, VMScript} = vm // 解包. 从解包中获取到VM和VMScript

var myvm = new VM()
let js_code = ""
// 1.补环境代码
var envCode = fs.readFileSync('C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\16 今日头条\\test\\补环境.js').toString();
//2. 源码
var sourceCode = fs.readFileSync('C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\16 今日头条\\test\\源码.js').toString()
//执行函数获取 sign window.byted_acrawler.sign(o)

// var get_sign_func_str = `var o = {'url':'http://123.com'};window.byted_acrawler.sign(o)`
debugger;
function getSign(url){
    js_code = envCode + '\n'+sourceCode+'\n'+`;o = {url:'${url}'};window.byted_acrawler.sign(o)`
    return myvm.run(js_code)
}
debugger;
console.log(getSign('123.com'))