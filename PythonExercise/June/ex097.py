"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/9
Description: 矩阵行平移
其使用数组实现最好，但这里只能用嵌套列表实现
"""
import sys


def transfer_list(lst, m, n):
    length = len(lst)
    for _ in range(m):
        lst.insert(0, n)
    return lst[:length]


N, k, x = map(int, sys.stdin.readline().split())
input_list = []
out_list = []
result_list = []
count = 1
for i in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))
for j in range(0, N, 2):
    input_list[j] = transfer_list(input_list[j], count, x)
    if count < k:
        count += 1
    else:
        count = 1

for m in range(N):
    sum = 0
    for n in range(N):
        sum += input_list[n][m]
    result_list.append(sum)

print(' '.join(list(map(str, result_list))))
