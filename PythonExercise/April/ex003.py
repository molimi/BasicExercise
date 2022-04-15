"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/14
Description: PAT自动裁判
判断条件：
1. 只能由P、A、T组成
2. P和T之间必须有A
3. P必须在T之前出现
4. T后面A的数量等于P前面A的数量乘以P和T之间A的数量
记录一个pos记录A出现的位置，count[0]记录P之前A出现的次数，
count[1]记录P和T之间A出现的次数，count[2]记录T之后A出现的次数
"""


def is_format(test_str):
    count_list = [0, 0, 0]
    pos = 0  # 刚开始默认从P之前开始记录
    for letter in test_str:
        if letter == 'A':
            count_list[pos] += 1  # 分别统计A在不同位置之间出现的次数
        elif letter == 'P' and pos == 0:  # 出现P之后，把pos置位1
            pos = 1
        elif letter == 'T' and pos == 1:  # 出现T之后，把pos置位2
            pos = 2
        else:
            return 'NO'
    # 判断T是否在P之后出现，P和T之间是否有A，以及T之后A的数量是否等于P&T之间A的数量乘以P前A的数量
    if pos == 2 and count_list[1] and count_list[
            2] == count_list[0] * count_list[1]:
        return 'YES'
    else:
        return 'NO'


def main():
    num = int(input())
    str_list = []

    for i in range(num):
        str_list.append(input())

    for test_str in str_list:
        print(is_format(test_str))


if __name__ == '__main__':
    main()