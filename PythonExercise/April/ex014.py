"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/21
Description: 福尔摩斯解码，日期用A-G表示，hour（0-23）用0-9和A-N表示，
minute用第一个相同字母的位置表示
"""
week_dict = {
    'A': 'MON',
    'B': 'TUE',
    'C': 'WED',
    'D': 'THU',
    'E': 'FRI',
    'F': 'SAT',
    'G': 'SUN'
}
str1 = input()
str2 = input()
str3 = input()
str4 = input()
length1 = min(len(str1), len(str2))
length2 = min(len(str3), len(str4))
res = []
flag1, flag2 = True, True
for i in range(length1):
    if flag1 and str1[i] == str2[i] and 'A' <= str1[i] <= 'G' and str1[
            i].isupper():
        res.append(str1[i])
        flag1 = False
    elif not flag1 and flag2 and str1[i] == str2[i] and (
            'A' <= str1[i] <= 'N'
            or '0' <= str1[i] <= '9') and (str1[i].isdigit()
                                           or str1[i].isupper()):
        res.append(str1[i])
        flag2 = False
        break

for j in range(length2):
    if str3[j] == str4[j] and str3[j].isalpha():
        if j in range(10):
            minute = '0' + str(j)
        else:
            minute = str(j)
        break

result = week_dict[res[0]] + ' '
if res[1].isalpha():
    result += str(ord(res[1]) - 55) + ':'
else:
    result += '0' + str(res[1]) + ':'
print('{}{}'.format(result, minute), end='')