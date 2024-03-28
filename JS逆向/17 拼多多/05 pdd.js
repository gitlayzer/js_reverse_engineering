// js入口执行文件

//加载文件
require("C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\17 拼多多\\01 env")
require("C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\17 拼多多\\02 mod1")
require("C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\17 拼多多\\02 mod2")
require("C:\\Users\\杨子洋\\PycharmProjects\\spiders\\JS逆向\\17 拼多多\\04 loader")

//调度fbez

function get_anti_content(){
    // 使用加载器调用
    window.loader("fbeZ")
    window.lt['updateServerTime'](new Date().getTime())
    return window.dt()

}

console.log(get_anti_content())