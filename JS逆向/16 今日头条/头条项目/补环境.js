
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
    protocol: 'https'
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

// function foo(){
//     console.log(window.href)
// }