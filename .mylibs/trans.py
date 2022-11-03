class Translation:
    def __init__(self):
        self.__s1 =  'abcdefghijklmnopqrstuvwxyz'
        self.__s2 = self.__s1.upper()

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
        n = str(n)[::-1]
        answer = 0
        for i in range(len(n)):
            if n[i] in self.__s1:
                j = 10 + self.__s1.index(n[i])
            elif n[i] in self.__s2:
                j = 10 + self.__s2.index(n[i])
            else:
                j = int(n[i])
            answer += j * x ** i
        return answer

    def x_x(self, n, x1, x2):
        return self.ten_x(self.x_ten(n, x1), x2)

trans = Translation()
