"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/9
Description: B是A的多少倍
"""

number1, n = input().split()
length = len(number1)
new_number = number1[length - int(n):] + number1[:length - int(n)]
print('{:.2f}'.format(int(new_number) / int(number1)))