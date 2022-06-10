"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 擅长C
注意：这里是大写字母，所以小写字母也要排除再外
"""

import re

letter_dict = {}
for i in range(26):
    letter_dict[chr(ord('A') + i)] = []
    for j in range(7):
        letter_dict[chr(ord('A') + i)].append(input())

str1 = input()
pattern = re.compile(r'[^A-Z]')
str1_list = pattern.split(str1)
str1_list = list(filter(lambda iter: iter and iter.strip(), str1_list))
length1 = len(str1_list)
for k in range(length1):
    length2 = len(str1_list[k])
    for p in range(7):
        for m in range(length2):
            if m < length2 - 1:
                print(letter_dict[str1_list[k][m]][p], end=' ')
            else:
                print(letter_dict[str1_list[k][m]][p])
    if k < length1 - 1:
        print()