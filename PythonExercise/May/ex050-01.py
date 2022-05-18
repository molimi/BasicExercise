"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/12
Description: 螺旋矩阵
思路：
计算m*n的矩阵，然后排列顺序并填充，
思路一：按一层一层来写，先上右下左
思路二：逐个元素填充
"""
from math import sqrt


def factorization(N):
    iter = int(sqrt(N))
    for i in range(iter, 0, -1):
        if N % i == 0:
            return N // i, i


def main():
    N = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort(reverse=True)
    m, n = factorization(N)
    top, right, bottom, left = 0, n - 1, m - 1, 0
    result_list = [[0 for j in range(n)] for i in range(m)]
    k = 0
    while (top <= bottom) and (left <= right):
        for j in range(left, right):  # 上边
            result_list[top][j] = input_list[k]
            k += 1
        for i in range(top, bottom + 1):  # 右边
            result_list[i][right] = input_list[k]
            k += 1
        # 考虑排到最后，可能没法组成一个框，只需要排一条边
        if (top < bottom) and (left < right):
            for p in range(right - 1, left, -1):  # 下边
                result_list[bottom][p] = input_list[k]
                k += 1
            for q in range(bottom, top, -1):  # 左边
                result_list[q][left] = input_list[k]
                k += 1
        top += 1
        right -= 1
        bottom -= 1
        left += 1
    for t in range(m):
        print(' '.join(list(map(str, result_list[t]))))


main()
'''
result_list = [[0 for i in range(n)]for i in range(m)]
for i in range(m):
    for j in range(n):
        result_list[i][j] = input_list[]
        '''