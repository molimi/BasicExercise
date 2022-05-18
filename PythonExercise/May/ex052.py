"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/15
Description: 输出表情
思路一：利用正则化表达式，先把多余字符拿掉
"""
# -*- coding: utf-8 -*-
'''
# 测试案例可以通过，但提交后总是非零返回
import re
import sys


# 不是空的字符串
def not_empty(str):
    return str and str.strip()


hand = re.split('[\[\]]', input())  # 利用正则表达式分割输入的字符串，得到表情
eye = re.split('[\[\]]', input())
mouth = re.split('[\[\]]', input())
hand = list(filter(not_empty, hand))  # 删掉空的字符串
eye = list(filter(not_empty, eye))
mouth = list(filter(not_empty, mouth))
len_hand = len(hand)   
len_eye = len(eye)
len_mouth = len(mouth)
N = int(input())
need_list = []
for j in range(N):
    need_list.append(list(map(int, input().split())))

for k in range(N):
    h1, e1, m, e2, h2 = need_list[k][0], need_list[k][1], need_list[k][
        2], need_list[k][3], need_list[k][4]
    if h1 < len_hand and h2 <= len_hand and e1 <= len_eye and e2 <= len_eye and m <= len_mouth:
        print('{}({}{}{}){}'.format(hand[h1 - 1], eye[e1 - 1], mouth[m - 1],
                                    eye[e2 - 1], hand[h2 - 1]))
    else:
        print('Are you kidding me? @\/@')
'''

# 按大家讲的，改用二进制
import sys

expression_list = []
for i in range(3):
    data = sys.stdin.buffer.readline()
    d = []
    s = bytes()
    for j in range(len(data)):
        if data[j] == b'[':
            s = bytes()
        if data[j] == b']':
            d.append(s)
        s += data[j]
    expression_list.append(s)

N = int(input())
need_list = []
for j in range(N):
    need_list.append(list(map(int, input().split())))