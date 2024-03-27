
`
在 JavaScript 中，可以使用 new 关键字创建对象，也可以使用字面量 {} 创建对象。

使用 new 关键字创建对象时，首先需要先定义一个构造函数，然后使用 new 关键字来调用构造函数，从而创建一个新的对象。例如：

`

// 方式一
function Person2(name,age){
    this.name = name;
    this.age = age
}

p2 = new Person2('yzy',15)

//方式二
var Person = {
    name: 'sb',
    age: 18
}

console.log(typeof Person) // object
console.log(typeof p2) // object

// 使用 new 关键字创建对象时，还可以使用原型链来实现继承等高级功能，而使用字面量创建的对象则不支持这些高级功能

var people= {
    name: 'sb',
    age : 18
}

function People(){

}
People.prototype.eat = function (){
    console.log('eating..')
}

Object.setPrototypeOf(people,People.prototype)
console.log(people)
// 此时people 已经是一个对象，并且有People属性，具有People的方法
people.eat() // eating..

