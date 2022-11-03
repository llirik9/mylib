from random import randint
from time import time


class Lib:
    def __init__(self):
        self.my_random = self.Random()
        self.my_time = self.Time()
        self.oge = self.Oge()
        self.sort = self.Sort()
        self.trans = self.Translation()


    class Time:
        def t(self, func):
            t1 = time()
            func()
            t2 = time()
            t3 = t2 - t1
            print(t3)


    class Oge:
        def __f(self, x):
            return x % self.__n == 0

        def oge(self, a, n, func):
            self.__n = n
            a = filter(self.__f, a)
            print(func(a))


    class Random:
        def randstr(self, n):
            al = 'abcdefghijklmnopqrstuvwxyz'
            al += al.upper()
            s = ''.join([al[randint(0, len(al)-1)] for i in range(n)])
            return s


    class Sort:
        def sort(self, list0):
            list1 = list0[:]
            list2 = []
            for i in range(len(list1)):
                list2.append(list1.pop(
                    list1.index(min(list1))
                ))
            return list2


    class Translation:
        def ten_x(self, n, x):
            n = int(n)
            answer = ''
            while n:
                i = n % x
                n = n // x
                if i >= 10:
                    i = self.__s1[i-10]
                answer += str(i)
            return answer[::-1]

        def x_ten(self, n, x):
            s1='abcdefghijklmnopqrstuvwxyz'
            s2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            n = str(n)[::-1]
            answer = 0
            for i in range(len(n)):
                if n[i] in s1:
                    j = 10 + s1.index(n[i])
                elif n[i] in s2:
                    j = 10 + s2.index(n[i])
                else:
                    j = int(n[i])
                answer += j * x ** i
            return answer

        def x_x(self, n, x1, x2):
            return self.ten_x(self.x_ten(n, x1), x2)

