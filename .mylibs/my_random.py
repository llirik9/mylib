from random import randint


class Random:
    def __init__(self):
        self.__al = 'abcdefghijklmnopqrstuvwxyz'
        self.__al += self.__al.upper()

    def randstr(self, n):
        s =''
        for i in range(n):
            s += self.__al[randint(0, len(al)-1)]
        return s


random = Random()

