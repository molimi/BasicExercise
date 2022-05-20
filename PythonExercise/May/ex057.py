"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/18
Description: 数零一
思路一：使用正则表达式
思路二：使用滤波器：filter(lambda s: s.isalpha(), str1)
"""

import re

pattern = re.compile(r'[^a-zA-Z]')
str1 = pattern.sub('', input())

str1 = str1.upper()
sum = 0
for i in range(len(str1)):
    sum += ord(str1[i]) - ord('A') + 1

# 想不明白为什么直接用bin(sum)有一个测试点不给通过，太神奇了，应该是编译器的原因，以后不能懒省事
number_0, number_1 = 0, 0
while sum:
    if sum % 2 == 1:
        number_1 += 1
    else:
        number_0 += 1
    sum = sum // 2

print('{} {}'.format(number_0, number_1))