"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 天长地久数
"""
import sys


# 判断素数
def is_primer(number):
    if number == 2 or number == 3:
        return True
    elif number == 1 or number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(6, int(number**0.5) + 2, 6):
        if number % (i - 1) == 0 or number % (i + 1) == 0:
            return False
            break
    return True


# 找最大公约数
def gcd(m, n):
    if m < n:
        m, n = n, m
    while n:
        if m % n == 0:
            return n
            break
        else:
            m, n = n, m % n


def sum_number(number):
    sum = 0
    while number:
        sum += number % 10
        number = number // 10
    return sum


def main():
    N = int(sys.stdin.readline())
    for i in range(N):
        K, sum1 = map(int, sys.stdin.readline().split())
        print('Case {}'.format(i + 1))
        out_list = []
        count = 10**(K - 1) + 999
        while count < 10**K - 1:
            if sum_number(count) == sum1:
                temp1 = sum_number(count + 1)
                temp2 = gcd(temp1, sum1)
                if temp2 > 2 and is_primer(temp2):
                    out_list.append((temp1, count))
            count += 1000
        length = len(out_list)
        out_list.sort(key=lambda item: (item[0], item[1]))
        if length:
            for j in range(length):
                sys.stdout.write('{} {}\n'.format(out_list[j][0],
                                                  out_list[j][1]))
        else:
            print('No Solution')


main()