"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/18
Description: 单词顺序颠倒输出
"""
word_list = input().split()
word_list[::-1]
result = ''
for word in word_list:
    result += word + ' '
print(result.strip())