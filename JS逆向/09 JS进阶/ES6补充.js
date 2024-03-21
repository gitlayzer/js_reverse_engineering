
//
// let name = 'yang'
// let age = 18
//
// function eat(){
//     console.log(`${this.name} 正在吃肉`)
// }
// let info = {
//     name,
//     age,
//     eat
//
// }
//
// info.eat()
//
// // 三元运算符
//
// let a = 10
// let b = 25
// // if (a>b){
// //     console.log(a)
// // }else{
// //     console.log(b)
// // }
// console.log(a>b?a:b)


let a = 10;
let b = 20;
let c = 5;
let d = 17;

let e;
let m;

e = (e = a > 3 ? b : c, m = e < b++ ? c-- : a = 3 > b % d ? 27: 37, m++)
// e = a > 3 ? b : c // e=b=20
// m = e < b++ ? c-- : a = 3 > b % d ? 27: 37// m=a=37
// e = m++ // e= 37 m=38
console.log(e);
console.log(c);
console.log(m);