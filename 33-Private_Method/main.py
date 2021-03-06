class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
        self.__private_method()

    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')

    def __private_method(self):
        print('private')

hello = Hello('name')
print(hello.a)
print(hello._b)
hello.public_method()
