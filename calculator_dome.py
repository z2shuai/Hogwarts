# 计算器(实现 加减乘除)
import math


class Calculator():
    def add(self, a, b):
        '''可以计算大数,浮点数,负数(精度保留3位)'''
        c = a + b
        print(c)
        if isinstance(c, int) or isinstance(c, str):
            return c
        else:
            return round(c, 3)

    def sub(self, a, b):
        '''可以计算大数,浮点数,负数(精度保留3位)'''
        c = a - b
        if isinstance(c, int) or isinstance(c, str):
            return c
        else:
            return round(c, 3)

    def mul(self, a, b):
        '''可以计算大数,浮点数,负数(精度保留3位)'''
        c = a * b
        if isinstance(c, int):
            return c
        else:
            return round(c, 3)

    def div(self, a, b):
        '''可以计算大数,浮点数,负数(精度保留3位),效验被除数不为0'''
        if b == 0:
            return "ZeroDivisionError"
        else:
            c = a / b
        if isinstance(c, int):
            return c
        else:
            return math.floor(c * 10 ** 3) / (10 ** 3)
