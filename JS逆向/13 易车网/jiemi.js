

function g() {
            return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                var t = 16 * Math.random() | 0
                  , n = "x" == e ? t : 3 & t | 8;
                return n.toString(16)
            })
        }

console.log(g())
//function l() {
//            var e = yicheUtils.getCookie("UserGuid") || yicheUtils.getCookie("CIGUID");
//            if (e)
//                return e;
//            var t = window.yicheUtils.createGuid();
//            return window.yicheUtils.setCookie("CIGUID", t, 43800, ".yiche.com"),
//            t
//        }