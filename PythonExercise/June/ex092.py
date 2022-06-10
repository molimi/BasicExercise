"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: 销量冠军
方法一：使用数组
方法二：使用嵌套列表
"""
'''
import numpy as np
M, N = map(int, input().split())
input_list = []
for i in range(N):
    input_list.append(list(map(int, input().split())))

input_array = np.array(input_list)
value = np.sum(input_array, axis=0)
max = value.max()
print(max)
result = ''
for j in range(M):
    if value[j] == max:
        result += str(j + 1) + ' '
print(result)
'''

M, N = map(int, input().split())
input_list = []
for i in range(N):
    input_list.append(list(map(int, input().split())))
value_list = [0 for _ in range(M)]
for j in range(M):
    for k in range(N):
        value_list[j] += input_list[k][j]

max = max(value_list)
print(max)
result = ''
for j in range(M):
    if value_list[j] == max:
        result += str(j + 1) + ' '
print(result)