"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/20
Description: 竞赛奖励
思路：发现一个问题利用列表的索引似乎没有字典的快，使用列表就会超时
"""
import math


# 素数相除法
def is_primer(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for k in range(6, int(math.sqrt(n)) + 2, 6):
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
    return True


def main():
    N = int(input())
    score_dict = {}
    for i in range(N):
        score_dict[input()] = i + 1
    K = int(input())
    for i in range(K):
        search = input()
        if search in score_dict:
            index = score_dict[search]
            if index == 0:
                print('{}: {}'.format(search, 'Checked'))
            else:
                if index == 1:
                    print('{}: {}'.format(search, 'Mystery Award'))
                elif is_primer(index):
                    print('{}: {}'.format(search, 'Minion'))
                else:
                    print('{}: {}'.format(search, 'Chocolate'))
            score_dict[search] = 0
        else:
            print('{}: {}'.format(search, 'Are you kidding?'))


main()
'''
def is_prime(number):
    if number == 1:
        return False
    sa = int(number**0.5) + 1
    for k in range(2, sa):
        if number % k == 0:
            return False
            break
    return True

def main():
    N = int(input())
    score_list = []
    for i in range(N):
        score_list.append(input())

    K = int(input())
    flag_list = [0 for i in range(N)]

    for k in range(K):
        search = input()
        if search in score_list:
            index = score_list.index(search)
            if flag_list[index]:
                print('{}: {}'.format(search, 'Checked'))
            else:
                if index == 0:
                    print('{}: {}'.format(search, 'Mystery Award'))
                elif is_primer(index + 1):
                    print('{}: {}'.format(search, 'Minion'))
                else:
                    print('{}: {}'.format(search, 'Chocolate'))
            flag_list[index] += 1
        else:
            print('{}: {}'.format(search, 'Are you kidding?'))


main()
'''