"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/15
Description: 输出数字换个格式
"""

number = int(input())
b = number // 100
s = number // 10 % 10
g = number % 10
result = b * 'B' + s * 'S'
for i in range(1, g + 1):
    result += str(i)
print(result)