"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/10
Description: 打印规定格式的字符串
思路：先统计字符的个数
"""
PATest = {'P': 0, 'A': 0, 'T': 0, 'e': 0, 's': 0, 't': 0}
str1 = input()
for item in str1:
    if item in PATest:
        PATest[item] += 1

result_str = ''
flag = True
while (PATest['P'] > 0) or (PATest['A'] > 0) or (PATest['T'] > 0) or (
        PATest['e'] > 0) or (PATest['s'] > 0) or (PATest['t'] > 0):
    if PATest['P'] > 0:
        result_str += 'P'
        PATest['P'] -= 1
    if PATest['A'] > 0:
        result_str += 'A'
        PATest['A'] -= 1
    if PATest['T'] > 0:
        result_str += 'T'
        PATest['T'] -= 1
        flag = False
    if PATest['e'] > 0:
        result_str += 'e'
        PATest['e'] -= 1
    if PATest['s'] > 0:
        result_str += 's'
        PATest['s'] -= 1
    if PATest['t'] > 0:
        result_str += 't'
        PATest['t'] -= 1
print(result_str)