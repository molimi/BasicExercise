"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 打印最大数量的沙漏
"""
from math import sqrt

n, sign = input().split()
N = int(n)
iteration = int(sqrt((N + 1) / 2))
ret = N - 2 * iteration**2 + 1
for i in range(iteration, 0, -1):
    print(' ' * (iteration - i) + sign * (2 * i - 1))

for j in range(1, iteration):
    print(' ' * (iteration - j - 1) + sign * (2 * j + 1))
print(ret)