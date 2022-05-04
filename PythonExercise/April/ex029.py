"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 监测漏掉的字符
"""

str1_list = list(input().upper())
str2_list = list(input().upper())
str_list = []
for i in range(len(str1_list)):
    if str1_list[i] in str2_list or str1_list[i] in str_list:
        continue
    else:
        str_list.append(str1_list[i])
print(''.join(str_list))