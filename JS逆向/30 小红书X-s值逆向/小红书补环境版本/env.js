
!(function(){
    "use strict";
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('',')_',(Math.random()+'').toString(36)));
    const mytoString = function(){
        return typeof this == 'function' && this[myFunction_toString_symbol] || $toString.call(this);
    };
    function set_native(func,key,value){
        Object.defineProperty(func,key,{
            "enumerable" : false,
            "configurable" : true,
            "writable" : true,
            "value" : value
        })
    };
    delete Function.prototype['toString'];
    set_native(Function.prototype,"toString",mytoString);
    set_native(Function.prototype.toString,myFunction_toString_symbol,"function toString() { [native code] }");
    this.func_set_native = function (func)  {
        set_native(func,myFunction_toString_symbol,`function ${myFunction_toString_symbol,func.name || ''}() { [native code] }`)
    }
}).call(this);

window = this;
delete global;

document = {
    getElementById:function getElementById(){console.log(arguments)},
    createElement:function createElement(tagname){
        console.log(arguments);
        if (typeof tagname !== 'string') {
            debugger;
            var aaaaaa = new Error('Failed to execute \'createElement\' on \'Document\': The tag name provided (\'[object HTMLDocument]\') is not a valid name.')
            aaaaaa.name = 'DOMException'
            aaaaaa = get_proxy(aaaaaa)
            throw aaaaaa
        }
        if (tagname && typeof tagname === 'string' && tagname.toUpperCase() === 'canvas'.toUpperCase())
        {
            var html_canvas_element = new HTMLCanvasElement();
            window.func_set_native(html_canvas_element.getContext);
            html_canvas_element = get_proxy(html_canvas_element)
            return html_canvas_element
        }
        else if (tagname && typeof tagname === 'string' && tagname.toUpperCase() === 'div'.toUpperCase())
        {
            var html_div_element = new HTMLDivElement()
            window.func_set_native(html_div_element.appendChild);
            html_div_element = get_proxy(html_div_element)
            return html_div_element
        }
        else if (tagname && typeof tagname === 'string')
        {
            var elementi = new HTMLAnchorElement(tagname)
            elementi = get_proxy(elementi)
            return elementi
        }
    },
    addEventListener:function addEventListener(){console.log(arguments)},
    cookie:'abRequestId=dafe1227-f736-5057-96a9-f31cf9a44753; a1=18d40069d4fa8j0x8fqaddxl85ic2h97a2bchdy7i50000356250; webId=f81524476908fa902552e338e511d6e6; gid=yYf488K0JY0YyYf488KjfJfv4i0YV8CYiA0fDW3fC1Y23S28SJxjWx888q2KJ288KSS8jSY8; unread={%22ub%22:%2265ab4958000000002e00507d%22%2C%22ue%22:%2265a47a81000000001d032d84%22%2C%22uc%22:25}; cache_feeds=[]; webBuild=4.1.6; xsecappid=小红书算法还原版-pc-web; websectiga=2a3d3ea002e7d92b5c9743590ebd24010cf3710ff3af8029153751e41a6af4a3; sec_poison_id=dbe6e2ab-d977-4467-9132-cceba71c91b4',
    referrer:'',
    visibilityState:'visible',
};



location = {
    href:'https://www.xiaohongshu.com/explore?channel_id=homefeed.movie_and_tv_v3',
    protocol:'https:',
    hostname:'www.xiaohongshu.com',
    host:'www.xiaohongshu.com',
    origin:'https://www.xiaohongshu.com',
    port:''
};


navigator = {
    plugins:[],
    languages:[
        "zh-CN",
        "zh"
    ],
    language:'zh-CN',
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    webdriver:false,
    vendorSub:'',
    productSub:'20030107',
    vendor:'Google Inc.',
    maxTouchPoints:0,
    scheduling:{},
    userActivation: {},
    doNotTrack:null,
    geolocation:{},
    connection:{},
    mimeTypes:{},
    pdfViewerEnabled:true,
    webkitTemporaryStorage:{},
    webkitPersistentStorage:{},
    hardwareConcurrency:12,
    cookieEnabled:true,
    appCodeName:'Mozilla',
    appName:'Netscape',
    appVersion:'5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    platform:'Win32',
    product:'Gecko',
    onLine:true,
    bluetooth:{},
    clipboard:{},
    credentials:{},
    keyboard:{},
    managed:{},
    mediaDevices:{},
    storage:{},
    serviceWorker:{},
    virtualKeyboard:{},
    wakeLock:{},
    deviceMemory:8,
    ink:{},
    hid:{},
    locks:{},
    mediaCapabilities:{},
    mediaSession:{},
    permissions:{},
    presentation:{},
    serial:{},
    gpu:{},
    usb:{},
    windowControlsOverlay:{},
    xr:{},
    userAgentData:{},
};


