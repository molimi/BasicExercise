"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 缘分数
"""
import math


def find_b(number):
    count = 2
    temp = count**2 + (count - 1)**2
    while temp <= number:
        if temp == number:
            return count
        count += 1
        temp = count**2 + (count - 1)**2
    return 0


m, n = map(int, input().split())
number1_list = []
number2_list = []
for i in range(m, n + 1):
    temp1 = i**3 - (i - 1)**3
    temp2 = math.sqrt(temp1)
    if temp2.is_integer():
        number1_list.append(i)
        number2_list.append(temp2)

length1 = len(number1_list)
out_list = []
if length1:
    for j in range(length1):
        temp3 = find_b(number2_list[j])
        if temp3:
            out_list.append((number1_list[j], temp3))
    length2 = len(out_list)
    if length2:
        for k in range(length2):
            print(out_list[k][0], out_list[k][1])
    else:
        print('No Solution')
else:
    print('No Solution')