

function Person(name,age){
    this.name =name
    this.age = age
}
Person.prototype.read = function (){
    console.log(this.name + 'is reading')
}
var p = new Person('tom',18)
var p2 = new Person('jerry',20)
console.log(p.name)
console.log(p2.age)
p2.read()
p.read()
console.log(Person.prototype) // { read: [Function (anonymous)] }

console.log(Person.prototype.constructor) // [Function: Person]

console.log(p2.__proto__)// { read: [Function (anonymous)] }

console.log(p2.__proto__.constructor)//[Function: Person]

