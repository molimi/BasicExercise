"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/9
Description: 性感素数
思路：注意可能会报错，如果N < 6就会有问题
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
    return True


def main():
    N = int(input())
    if N > 6 and is_primer(N) and is_primer(N - 6):
        print('Yes')
        print(N - 6)
    elif is_primer(N) and is_primer(N + 6):
        print('Yes')
        print(N + 6)
    else:
        print('No')
        flag = False
        while True:
            N += 1
            if N > 6 and is_primer(N) and is_primer(N - 6):
                flag = True
            elif is_primer(N) and is_primer(N + 6):
                flag = True
            if flag:
                break
        print(N)


main()