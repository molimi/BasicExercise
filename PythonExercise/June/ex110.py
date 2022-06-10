"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 区块翻转
问题：测试点五超时，暂时没想到用Python有更好地解决方案
"""
import sys


def prefix(lst1, lst2):
    lst = lst1[:]
    for i in range(len(lst2) - 1, -1, -1):
        lst.insert(0, lst2[i])
    return lst


def reverse_list(linked_dict, K, add_node):
    out_list = []
    node_list = []
    while add_node != '-1':  # 没到链表结束，继续循环
        sub_data = []
        sub_node = []
        for i in range(K):  # 每K个循环一次
            if add_node != '-1':
                sub_data.append(linked_dict.get(add_node))
                sub_node.append(add_node)
                add_node = sub_data[i][2]

        out_list = prefix(out_list, sub_data)
        node_list = prefix(node_list, sub_node)
    node_list.append('-1')
    for i in range(len(out_list)):
        sys.stdout.write('{} {} {}\n'.format(out_list[i][0], out_list[i][1],
                                             node_list[i + 1]))


def main():
    init_node, N, K = input().split()
    linked_dict = {}
    for _ in range(int(N)):
        address, data, next = sys.stdin.readline().split()
        linked_dict[address] = (address, data, next)
    reverse_list(linked_dict, int(K), init_node)


main()