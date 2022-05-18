"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 有理数的四则运算
Tips：  一、初始化数据
        二、显示数据
        三、加减乘除运算
"""


class RationalFraction(object):

    def __init__(self, top, bottom=1):
        self.top = top
        self.bottom = bottom
        if top * bottom < 0:
            self.flag = 1  # 表示为负数
        else:
            self.flag = 0

    def show(self):
        top, bottom = self.top, self.bottom
        if bottom == 0:
            return 'Inf'
        elif top == 0:
            return '0'
        elif top % bottom == 0:
            result = top // bottom
            return '(' + str(result) + ')' if self.flag else str(result)
        max_factor = gcd(top, bottom)
        top, bottom = top // max_factor, bottom // max_factor
        if abs(top) < abs(bottom):
            return '(' + str(top) + '/' + str(
                bottom) + ')' if self.flag else str(top) + '/' + str(bottom)
        else:
            if self.flag:
                return '(-' + str(abs(top) // bottom) + ' ' + str(
                    abs(top) % bottom) + '/' + str(bottom) + ')'
            else:
                return str(top // bottom) + ' ' + str(
                    top % bottom) + '/' + str(bottom)

    def __add__(self, other):
        top = self.top * other.bottom + self.bottom * other.top
        bottom = self.bottom * other.bottom
        if top == 0:
            return RationalFraction(0)
        else:
            max_factor = gcd(top, bottom)
            return RationalFraction(top // max_factor, bottom // max_factor)

    def __sub__(self, other):
        top = self.top * other.bottom - self.bottom * other.top
        bottom = self.bottom * other.bottom
        if top == 0:
            return RationalFraction(0)
        else:
            max_factor = gcd(top, bottom)
            return RationalFraction(top // max_factor, bottom // max_factor)

    def __mul__(self, other):
        top = self.top * other.top
        bottom = self.bottom * other.bottom
        if top == 0:
            return RationalFraction(0)
        else:
            max_factor = gcd(top, bottom)
            return RationalFraction(top // max_factor, bottom // max_factor)

    def __truediv__(self, other):
        top = self.top * other.bottom
        bottom = self.bottom * other.top
        if bottom == 0:
            return RationalFraction(0, 0)
        if top == 0:
            return RationalFraction(0)
        else:
            max_factor = gcd(top, bottom)
            if top * bottom < 0:
                return RationalFraction(-abs(top) // max_factor,
                                        abs(bottom) // max_factor)
            else:
                return RationalFraction(top // max_factor,
                                        bottom // max_factor)


def gcd(m, n):  # 欧几里得算法，找最大公约数
    m, n = abs(m), abs(n)
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m % n
    return n


str1, str2 = input().split()
a, b = map(int, str1.split('/'))
c, d = map(int, str2.split('/'))
x1 = RationalFraction(a, b)
x2 = RationalFraction(c, d)
print(x1.show() + ' + ' + x2.show() + ' = ' + (x1 + x2).show())
print(x1.show() + ' - ' + x2.show() + ' = ' + (x1 - x2).show())
print(x1.show() + ' * ' + x2.show() + ' = ' + (x1 * x2).show())
print(x1.show() + ' / ' + x2.show() + ' = ' + (x1 / x2).show())