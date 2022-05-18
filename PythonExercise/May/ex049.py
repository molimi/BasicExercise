"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/12
Description: 片段求和
思路一：暴力解法，肯定超时
思路二：找规律
bug：测试点二可能没法通过，出现测试点2一直报错，
原因时超出了float的表示范围，需要使用精确度更高的Decimal来计算。
"""
import sys
'''
def sum_list(lst):
    result = 0
    for i in range(len(lst)):
        result += sum(lst[:i + 1])
    return result


def main():
    n = int(input())
    input_list = list(map(float, sys.stdin.readline().split()))
    result = 0
    for i in range(n):
        result += sum_list(input_list[i:])
    print('{:.2f}'.format(result))


main()
'''

# 发现规律每个元素的个数为(i+1)*(n-i)
import sys
from decimal import Decimal


def main():
    n = int(input())
    input_list = list(map(Decimal, sys.stdin.readline().split()))
    result = 0
    for i in range(n):
        result += input_list[i] * (i + 1) * (n - i)
    print('{:.2f}'.format(result))


main()