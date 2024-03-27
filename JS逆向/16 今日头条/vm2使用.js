var vm = require("vm2")

const {VM, VMScript} = vm

var myvm = new VM()

// ret = myvm.run("process")
// console.log(ret)

ret = myvm.run("1+2")
console.log(ret)