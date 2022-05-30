"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/28
Description: 字符串压缩与解压
题意简单，但通过测试比较坑，首先第一个如果解压缩时，只有0，那肯定输入空字符串，空格也算字符，
使用isalpha()只会统计字母，其次可能输入为100s，这时也要判断什么时候为字母
"""
str1 = input()
deal_str = input()
out_str = ''
length = len(deal_str)
if str1 == 'C':
    i = 0
    temp = deal_str[0]
    count = 1
    while i < length - 1:
        i += 1
        if temp == deal_str[i]:
            count += 1
        else:
            if count > 1:
                out_str += str(count) + temp
            else:
                out_str += temp
            temp = deal_str[i]
            count = 1
    else:
        if count > 1:
            out_str += str(count) + temp
        else:
            out_str += temp

elif str1 == 'D':
    j = 0
    if deal_str != '0':
        while j < length - 1:
            if deal_str[j].isdigit():
                if not deal_str[j + 1].isdigit():
                    out_str += int(deal_str[j]) * deal_str[j + 1]
                    j += 2
                else:
                    if not deal_str[j + 2].isdigit():
                        out_str += int(deal_str[j:j + 2]) * deal_str[j + 2]
                        j += 3
                    else:
                        out_str += int(deal_str[j:j + 3]) * deal_str[j + 3]
                        j += 4
            else:
                out_str += deal_str[j]
                j += 1
        if j == length - 1:
            out_str += deal_str[-1]

print(out_str)