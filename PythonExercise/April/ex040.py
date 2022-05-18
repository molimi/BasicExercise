"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/6
Description: PAT个数
"""
# 思路一，暴力一点，直接遍历，果然超时了
'''
str1_list = input()
length = len(str1_list)
count = 0
for i in range(length):
    if str1_list[i] == 'P':
        for j in range(i, length):
            if str1_list[j] == 'A':
                for k in range(j, length):
                    if str1_list[k] == 'T':
                        count += 1

print(count % 1000000007)
'''

# 思路二：记住A前面P的个数，A后面T的个数
'''
先把输入的字符串转换成列表，并逆序，先统计T的数量，如果遇到A，就是AT的数量，遇到P就是PAT的数量
'''
import sys

str1_list = list(sys.stdin.readline())
str1_list.reverse()
count_T = 0
count_AT = 0
count_PAT = 0
for item in str1_list:
    if item == 'T':
        count_T += 1
    elif item == 'A':
        count_AT += count_T
    else:
        count_PAT += count_AT
print(count_PAT % 1000000007)