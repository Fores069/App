class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

p1 = Person('Max', 21)
p1.old=233
p1.name = "Misha"


class User:

    def __init__(self, name, psw):
        self.name = name
        self.psw = psw

    def __getattribute__(self, item):
        if item == 'psw':
            raise ValueError('Пароль недоступен для пользователя уровня qzartion')
        else:
            res = object.__getattribute__(self, item)
            return res

    def __setattr__(self, key, value):
        print('Вызов __setattr__')
        object.__setattr__(self, key, value)


us1 = User(12.5, 1234)
us1.lvl = 12.5
