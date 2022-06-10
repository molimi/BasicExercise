"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: 谷歌招聘
bug: 考虑需要的位数大于输入的位数
"""


def is_primer(number):
    if number == 2 or number == 3:
        return True
    elif number == 1 or number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(6, int(number**0.5) + 2, 6):
        if number % (i - 1) == 0 or number % (i + 1) == 0:
            return False
            break
    else:
        return True


def main():
    L, K = map(int, input().split())
    N = input()
    if L < K:
        print(404)
    else:
        flag = False
        for i in range(L - K + 1):
            number = int(N[i:i + K])
            if is_primer(number):
                flag = True
                print(N[i:i + K])
                break
        if not flag:
            print(404)


main()