function func(arg) {
    return arg + 'i666';
}
var a1 = process.argv[0]
var data = func(a1);
console.log(data)

function letValidate() {
    var url = "/Login/GetValidateCode/" + (new Date()).getTime();
    return url;
    }

