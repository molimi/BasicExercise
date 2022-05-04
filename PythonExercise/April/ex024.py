"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 科学计数法
思路：看似考察数字转换，其实是字符产拼接，一上来就陷入误区
"""

number_str, index_str = input().split('E')
sign = '' if number_str[0] == '+' else '-'
integer_str, decimal_str = number_str[1:].split('.')
if int(index_str) == 0:
    print(number_str)
elif index_str[0] == '+':
    temp = int(index_str) - len(decimal_str)
    if temp >= 0:
        print(sign + integer_str + decimal_str + '0' * temp)
    else:
        print(sign + integer_str + decimal_str[:int(index_str)] + '.' +
              decimal_str[int(index_str):])
else:
    print(sign + '0' + '.' + '0' * int(index_str[1:] - 1) + integer_str +
          decimal_str)
