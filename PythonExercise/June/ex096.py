"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/8
Description: 大美数
思路：先找因数
知识点：每个break只能结束一个循环，所以想要结束多个循环，必须加break
这里好像用while循环更简单一些
"""


def factor(number):
    lst = [1]
    for i in range(2, number):
        if number % i == 0:
            lst.append(i)
    lst.append(number)
    return lst


def main():
    K = int(input())
    input_list = list(map(int, input().split()))
    for j in range(K):
        temp = factor(input_list[j])
        length = len(temp)
        if length < 4:
            print('No')
        else:
            flag = False
            for m in range(length - 3):
                if flag:
                    break
                for n in range(m + 1, length - 2):
                    if flag:
                        break
                    for p in range(n + 1, length - 1):
                        if flag:
                            break
                        for q in range(p + 1, length):
                            sum = temp[m] + temp[n] + temp[p] + temp[q]
                            if sum % input_list[j] == 0:
                                flag = True
                                break
                            else:
                                flag = False
            if flag:
                print('Yes')
            else:
                print('No')


main()