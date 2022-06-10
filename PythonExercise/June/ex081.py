"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 检查密码
思路：一、使用正则表达式；二、每个字符遍历
"""
import re
pattern1 = re.compile(r'^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9\.]{6,}$')
pattern2 = re.compile(r'^(?=.*[a-zA-Z])[a-zA-Z\.]{6,}$')
pattern3 = re.compile(r'^(?=.*\d)[0-9\.]{6,}$')
N = int(input())
for i in range(N):
    temp = input().strip()
    length = len(temp)
    if length < 6:
        print('Your password is tai duan le.')
    elif pattern1.match(temp):
        print('Your password is wan mei.')
    elif pattern2.match(temp):
        print('Your password needs shu zi.')
    elif pattern3.match(temp):
        print('Your password needs zi mu.')
    else:
        print('Your password is tai luan le.')