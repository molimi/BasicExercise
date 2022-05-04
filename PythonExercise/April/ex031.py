"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 身份证号
"""
import re

weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2', '1']
n = int(input())
pattern = re.compile(r'(^\d{18}$)|(^\d{17})(\d|X)$')
result_list = []
for i in range(n):
    input_str = input()
    match = pattern.match(input_str)
    if match:
        input_list = list(input_str)
        sum = 0
        for i in range(17):
            sum += int(input_list[i]) * weights[i]
        z = sum % 11
        if input_list[-1] == m[z]:
            continue
        else:
            result_list.append(input_str)
    else:
        result_list.append(input_str)

if result_list == []:
    print('All passed')
else:
    for item in result_list:
        print(item)