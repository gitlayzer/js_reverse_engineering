

function f(x){
    return x*x
}

var res = f(2)
console.log(res)

// 箭头函数

f2 = x => x*x
res2 = f2(5)
console.log(res2)

let arr = [1,3,5]
arr1=arr.map(function (item){return item*item*item})
console.log(arr1)
arr2 = arr.map(item =>item*item*item*item)
console.log(arr2)