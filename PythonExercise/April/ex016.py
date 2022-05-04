"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/23
Description: 德才兼备
"""


def numberfraction(number):
    number_list = []
    while number:
        number_list.append(number % 10)
        number = number // 10
    return number_list


def main():
    [A, DA, B, DB] = list(map(int, input().split()))
    a_list = numberfraction(A)
    b_list = numberfraction(B)
    result1, result2 = 0, 0
    for i in range(a_list.count(DA)):
        result1 = result1 + DA * 10**(i)
    for j in range(b_list.count(DB)):
        result2 = result2 + DB * 10**(j)
    print(result1 + result2)


if __name__ == '__main__':
    main()