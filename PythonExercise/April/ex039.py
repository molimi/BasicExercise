"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/6
Description: 串珠子
"""
str1 = input()
str2 = input()
sale_dict = {}
buy_dict = {}
length1 = len(str1)
length2 = len(str2)

for i in range(length1):
    if str1[i] in sale_dict:
        sale_dict[str1[i]] += 1
    else:
        sale_dict[str1[i]] = 1
for j in range(length2):
    if str2[j] in buy_dict:
        buy_dict[str2[j]] += 1
    else:
        buy_dict[str2[j]] = 1

count = 0
for item in buy_dict:
    if item in sale_dict:
        if buy_dict[item] <= sale_dict[item]:
            continue
        else:
            count += buy_dict[item] - sale_dict[item]
    else:
        count += buy_dict[item]

if count:
    print('No' + ' ' + str(count))
else:
    print('Yes' + ' ' + str(length1 - length2))