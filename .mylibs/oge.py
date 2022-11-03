class Oge:
    def __init__(self):
        pass


    def __f(self, x):
        return x % self.__n == 0


    def oge(self, a, n, func):
        self.__n = n
        a = filter(self.__f, a)
        print(func(a))


oge = Oge()
