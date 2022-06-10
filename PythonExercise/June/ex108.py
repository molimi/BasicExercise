"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: String复读机
"""
str1_list = list(input())
str2_list = [['S', 0], ['t', 0], ['r', 0], ['i', 0], ['n', 0], ['g', 0]]
for i in range(6):
    str2_list[i][1] = str1_list.count(str2_list[i][0])
result = ''
while (str2_list[0][1] or str2_list[1][1] or str2_list[2][1] or str2_list[3][1]
       or str2_list[4][1] or str2_list[5][1]):
    if str2_list[0][1]:
        result += 'S'
        str2_list[0][1] -= 1
    if str2_list[1][1]:
        result += 't'
        str2_list[1][1] -= 1
    if str2_list[2][1]:
        result += 'r'
        str2_list[2][1] -= 1
    if str2_list[3][1]:
        result += 'i'
        str2_list[3][1] -= 1
    if str2_list[4][1]:
        result += 'n'
        str2_list[4][1] -= 1
    if str2_list[5][1]:
        result += 'g'
        str2_list[5][1] -= 1
print(result)