"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 打印字符
"""
str1 = list(input().lower())
str2 = input()
new_str = ''
for i in range(len(str2)):
    if '+' in str1 and str2[i].isupper():
        continue
    elif str2[i].lower() in str1:
        continue
    else:
        new_str += str2[i]
print(new_str)