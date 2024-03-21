foo = (function () {
        var key = '123456'

        function setKey(key) {
            return key + '789'
        }

        function foo() {
            new_key = key + setKey()
            console.log('foo的key', new_key)
        }

        return foo
    }
)()


bar = (function () {
        var key = 'dhfbeg'

        function setKey(key) {
            return key + 'adfadf'
        }

        function foo() {
            new_key = key + setKey()
            console.log('bar的key', new_key)
        }

        return foo
    }
)()
foo()
bar()
