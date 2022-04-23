"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/16
Description: 素数对猜想
"""
from math import sqrt


def is_primer(number):
    n = int(sqrt(number)) + 1
    if number == 1 or number == 0:
        return False
    else:
        for i in range(2, n):
            if number % i == 0:
                return False
                break
        return True


number = int(input())
primer_list = []
for i in range(2, number + 1):
    if is_primer(i):
        primer_list.append(i)

count = 0
for i in range(len(primer_list) - 1):
    if (primer_list[i + 1] - primer_list[i]) == 2:
        count += 1

print(count)