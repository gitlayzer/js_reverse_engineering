
require('./env')
require('./mod1')
require('./loader')
function getSign(data){
    return window.loader(147).default(data)
}
// var data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921504811854453","g_tk_new_20200303":34196356,"g_tk":34196356},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.center","searchid":"58786819462806779","search_type":0,"query":"梨花香","page_num":1,"num_per_page":10}}}'
// console.log(window.loader(147).default(data))