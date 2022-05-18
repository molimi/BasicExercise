"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 插入排序和归并排序
"""


def InsertSort(sort_list, compare_list):
    sort_list = sort_list[:]
    flag = False
    for i in range(2, len(sort_list) + 1):
        sort_list[0:i] = sorted(sort_list[0:i])
        if flag:
            print('Insertion Sort')
            print(' '.join(list(map(str, sort_list))))
            break
        if sort_list == compare_list:
            flag = True


def MergeSort(sort_list, compare_list):
    # 由于判断排序方式会对列表的本身产生改变，为了不影响进一步的判断，
    # 创建新的列表来保存要进行排序的数据
    sort_list = sort_list[:]
    length = len(sort_list)
    gap = 1
    flag = False
    while gap < length:
        gap = gap * 2  # 每次循环归并列表的长度都要大一倍
        i = 0  # 当gap与待排序列表长度length相同时，for循环无法启动，所以预先设置i为0
        for i in range(gap, length, gap):
            sort_list[i - gap:i] = sorted(sort_list[i - gap:i])
        sort_list[i:] = sorted(sort_list[i:])  # 当剩下的长度不够一个归并列表段时，将剩下的部分排序
        if flag:
            print('Merge Sort')
            print(' '.join(list(map(str, sort_list))))
            break
        if sort_list == compare_list:
            flag = True


def main():
    n = int(input())
    sort_list = list(map(int, input().split()))
    compare_list = list(map(int, input().split()))
    lst1 = [9, 12, 6, 4, 5, 8, 2, 1, 7, 10, 11]
    lst2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    MergeSort(sort_list, compare_list)
    InsertSort(sort_list, compare_list)


main()