"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/6
Description: 打印字符
"""
from math import ceil

n, character = input().split()
number = int(n)
iteration = ceil(number / 2)
for i in range(iteration):
    if i == 0 or i == iteration - 1:
        print(character * number)
    else:
        print(character + ' ' * (number - 2) + character)