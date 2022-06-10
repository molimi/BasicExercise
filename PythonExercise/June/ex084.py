"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 外观数列
"""


def rule(input_str):
    length = len(input_str)
    temp = input_str[0]
    count = 1
    i = 0
    result = ''
    while i < length - 1:  # 把前一个暂存，后一项与前一项比较，最后把后一项加上
        i += 1
        if temp == input_str[i]:
            count += 1
        else:
            result += temp + str(count)
            temp = input_str[i]
            count = 1
    else:
        result += temp + str(count)
    return result


def main():

    d, N = input().split()
    ans = d
    for i in range(1, int(N)):
        ans = rule(ans)
    print(ans)


main()