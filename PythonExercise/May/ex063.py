"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 计算谱半径
"""
from math import sqrt
N = int(input())
result_list = []
for i in range(N):
    real, imag = list(map(int, input().split()))
    result_list.append(sqrt(real**2 + imag**2))

print('{:.2f}'.format(max(result_list)))