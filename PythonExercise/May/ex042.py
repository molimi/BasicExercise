"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/10
Description: 统计字符
思路：
利用正则化去掉多余的字符，只保留英文字母，然后建一个字典
"""
import re
pattern = re.compile(r'[\W]|\d')
str1 = input()
str1 = pattern.sub('', str1)
str1 = str1.lower()
word_dict = {}
for item in str1:
    if item in word_dict:
        word_dict[item] += 1
    else:
        word_dict[item] = 1

word_order = sorted(word_dict.items(),
                    key=lambda item: (item[1], -ord(item[0])))
print(word_order[-1][0] + ' ' + str(word_order[-1][1]))