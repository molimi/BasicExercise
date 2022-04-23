"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/21
Description: 输入M和N，PM和PN表示第M和第N个素数，
输出PM和PN之间的所有素数，每十个数字占一行
"""
import math

[m, n] = list(map(int, input().split()))
'''
这个方法判断素数效率比较低效
def is_primer(number):
    num = int(math.sqrt(number)) + 1
    if number == 1 or number == 0:
        return False
    else:
        for i in range(2, num):
            if number % i == 0:
                return False
                break
        else:
            return True
'''


# 方法二：可以让一个数只除以素数
def is_primer(number):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(6, int(math.sqrt(number)) + 2, 6):
        if number % (i - 1) == 0 or number % (i + 1) == 0:
            return False
    return True


i, j, k = 0, 0, 0

while True:
    i += 1
    if is_primer(i):
        j += 1
        if j <= m:
            continue
        elif j <= n + 1:
            k += 1
            if k % 10 == 0:
                print(i)
            else:
                if k == n - m + 1:
                    print(i)
                else:
                    print(i, end=' ')
        else:
            break