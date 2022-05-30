"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/25
Description: 多进制加法器
bug: 这里主要是输出要注意，一、行尾有数字，行首有0不合法，二、行尾无数字，需要输出0
"""


def number_split(number_str):
    number_list = list(map(int, list(number_str)))
    number_list.reverse()
    return number_list


input_str = input()
number_one = input()
number_two = input()
base_list = number_split(input_str)
one_list = number_split(number_one)
two_list = number_split(number_two)
length1 = len(one_list)
length2 = len(two_list)
length = len(base_list)
one_list = one_list + [0] * (length - length1)
two_list = two_list + [0] * (length - length2)
previous = 0
result_list = []
for i in range(length):
    sum = one_list[i] + two_list[i] + previous
    base = base_list[i]
    if base == 0:
        base = 10
    previous = sum // base
    latter = sum % base
    result_list.append(latter)
result_list.append(previous)  # 反正最后要删除0，所以无所谓判断previous
result_list.reverse()
result = ''.join(map(str, result_list))
result = result.lstrip('0')  # 把开头的0删除
if result:
    print(result)
else:
    print(0)  # 如果只有零，就输出0
