# coding: utf-8

# import subprocess


# res = subprocess.check_output('node v1.js',shell=True)
# print(res.decode())


import execjs

js_string = """
function func(arg) {
    return arg + '\t'+'i666';
}
var a1 = process.argv[1]
var data = func(a1);
console.log(data)
"""

JS = execjs.compile(js_string)
res = JS.call("func",'sb')
print(res)