from time import time

class Time:
    def __init__(self):
        self.__t1 = 0
        self.__t2 = 0
        self.__t3 = 0

    def t(self, func):
        self.__t1 = time()
        func()
        self.__t2 = time()
        self.__t3 = self.__t2 - self.__t1
        print(self.__t3)


time = Time()
