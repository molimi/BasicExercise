"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/14
Description: 读入一个正整数 n，计算其各位数字之和，
用汉语拼音写出和的每一位数字。
"""
input_number = input()
number_dict = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'
}
sum = 0
result = ''
for iter in input_number:
    sum += int(iter)

for item in str(sum):
    result += number_dict[item] + ' '

print(result.strip())