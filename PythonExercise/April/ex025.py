"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 翻转列表
思路：节点地址、数据、下一节点地址
"""


# 两个遍历进行实现
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
            else:
                sub_data.reverse()
                sub_node.reverse()
                break  # 最后不够K个结束循环
        sub_data.reverse()
        sub_node.reverse()
        out_list.extend(sub_data)
        node_list.extend(sub_node)
    node_list.append('-1')
    for i in range(len(out_list)):
        print('{} {} {}'.format(out_list[i][0], out_list[i][1],
                                node_list[i + 1]))


init_node, N, K = input().split()
linked_dict = {}
for i in range(int(N)):
    address, data, next = input().split()
    linked_dict[address] = (address, data, next)
reverse_list(linked_dict, int(K), init_node)