"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/20
Description: 求给定两个分数之间分母为K的最简分数
思路一：找最小公倍数和最大公约数
"""
import re


# 辗转相除法
def gcd(m, n):
    if m < n:
        m, n = n, m

    while n:
        res = m % n
        m, n = n, res
    return m


fraction1, fraction2, fraction3 = input().split()

high1, low1 = list(map(int, fraction1.split('/')))
high2, low2 = list(map(int, fraction2.split('/')))
K = int(fraction3)
high_one = high1 * low2 * K
high_two = high2 * low1 * K
if high_one < high_two:
    high_one, high_two = high_two, high_one
flag = True
times = 1
result_list = []
while flag:
    temp = low1 * low2 * times
    if temp <= high_two:
        times += 1
    elif temp < high_one and temp > high_two:
        result_list.append(times)
        times += 1
    else:
        flag = False

result = ''
for i in range(len(result_list)):
    if gcd(result_list[i], K) == 1:
        result += str(result_list[i]) + '/' + fraction3 + ' '
print(result.strip())