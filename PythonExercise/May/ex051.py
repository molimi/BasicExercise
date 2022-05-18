"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/12
Description: 复数的乘积
思路：写一个复数的类，属性real和imag
方法一：乘法，返回形式
bug：题目简单，但需要考虑实部和虚部为零的情况，还有就是保留两位小数，当实部或虚部小于0.005
有个小坑就是，最后输出为-0.001时，应该打印为0.00，而不是-0.00
"""
from math import cos, sin


class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def Multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        if abs(self.imag) < 0.05:  # 当虚部绝对值小于0.005时，应该置位0
            self.imag = 0
        if abs(self.real) < 0.05:  # 实部绝对值小于0.005时，应该置位0
            self.real = 0
        if self.imag < 0:
            return '{:.2f}'.format(self.real) + '{:.2f}'.format(
                self.imag) + 'i'
        else:
            return '{:.2f}'.format(self.real) + '+' + '{:.2f}'.format(
                self.imag) + 'i'


def Convert(R, P):
    return R * cos(P), R * sin(P)


def main():
    input_list = list(map(float, input().split()))
    real1, imag1 = Convert(input_list[0], input_list[1])
    real2, imag2 = Convert(input_list[2], input_list[3])
    complex1 = Complex(real1, imag1)
    complex2 = Complex(real2, imag2)
    print(complex1.Multiply(complex2))


main()