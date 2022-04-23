"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/18
Description: 数组元素循环右移，第一行输入元素个数和回滚个数，第二行输入数组
"""

[m, n] = [int(x) for x in input().split(' ')]
result = ''
number_list = [int(x) for x in input().split(' ')]

for i in range(n):
    ans = number_list.pop()
    number_list.insert(0, ans)

for j in range(m):
    result += str(number_list[j]) + ' '
print(result.strip())