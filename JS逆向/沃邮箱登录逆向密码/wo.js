
require("D:\\JS逆向\\spiders\\JS逆向\\沃邮箱登录逆向密码\\env")
require("D:\\JS逆向\\spiders\\JS逆向\\沃邮箱登录逆向密码\\mod1")
require("D:\\JS逆向\\spiders\\JS逆向\\沃邮箱登录逆向密码\\loader")

var t = '123456'
var o = "9fd70fe812b180bc13a62df49fdf32884c831434fcb0abe6a55ddd49a4b99fcbff3112477d1fe398fe66ece13c19881fe72c4814b732a3d126c13fdd67ae7846c43a3a36e8e0a19b01dfc4a7929e17164b3718b5caf6d4b5b08f9684cf646cf4a54c3c5fc283f40f38aaf5bc7d5baaad6a046634deffe72b98c5f57b1fef2401"
var n = '10001'

console.log(window.loader('437').encrypt(t, o, n))