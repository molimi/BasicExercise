"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 有理数的四则运算
"""


def fraction(a, b):
    if a > b:
        k = a // b
        c = a % b
    elif a == b:
        k = 1
        c = 0
    else:
        k = 0
        c = a
    return k, c


str1, str2 = input().split()
a, b = map(int, str1.split('/'))
k, c = fraction(a, b)
if k < 0:
    print('({} {}/{})'.format(k, c, b))
elif k == 0 and c < 0:
    print('({}/{})'.format(c, b))