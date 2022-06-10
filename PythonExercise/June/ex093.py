"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: 字符串相加
思路一：直接两个同时遍历
思路二：使用字典排序
"""
'''
str1 = input()
str2 = input()
result_list = []
for i in range(len(str1)):
    if str1[i] in result_list:
        continue
    else:
        result_list.append(str1[i])
for j in range(len(str2)):
    if str2[j] in result_list:
        continue
    else:
        result_list.append(str2[j])
print(''.join(result_list))
'''
str1 = input()
str2 = input()
input_str = str1 + str2
result_dict = {}
count = 1
for i in range(len(input_str)):
    if input_str[i] in result_dict.keys():
        continue
    else:
        result_dict[input_str[i]] = count
        count += 1
print(''.join(result_dict.keys()))