"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/10
Description: 火星文格式转换
思路：先统计字符的个数
"""


def main():
    low_list = [
        'tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep',
        'oct', 'nov', 'dec'
    ]
    high_list = [
        'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok',
        'mer', 'jou'
    ]
    n = int(input())
    input_list = []
    for i in range(n):
        input_list.append(input())
    for j in range(n):
        if input_list[j].isdigit():
            input_number = int(input_list[j])
            high = input_number // 13
            low = input_number % 13
            if high == 0:
                print(low_list[low])
            elif low == 0:
                print(high_list[high - 1])
            else:
                print(high_list[high - 1] + ' ' + low_list[low])
        else:
            lst1 = input_list[j].split()
            length = len(lst1)
            if length == 2:
                print((high_list.index(lst1[0]) + 1) * 13 +
                      low_list.index(lst1[1]))
            else:
                if lst1[0] in low_list:
                    print(low_list.index(lst1[0]))
                else:
                    print((high_list.index(lst1[0]) + 1) * 13)


main()