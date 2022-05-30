"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/25
Description: 链表元素分类
思路：非负元素都排在前面，然后大于K的元素排在后面，且保证内部顺序不改变
Bug：存在废弃数据，需要剔除
字典使用dict.get(key)和dict[key]返回值不一样
"""
import sys
init_node, N, K = sys.stdin.readline().split()
linked_dict = {}
for i in range(int(N)):
    address, data, next = sys.stdin.readline().split()
    linked_dict[address] = (address, data, next)

add_node = init_node
out_list_one = []
out_list_two = []
out_list_three = []
node_list_one = []
node_list_two = []
node_list_three = []
out_list = []
node_list = []
while add_node != '-1':
    temp = int(linked_dict[add_node][1])
    if temp < 0:
        out_list_one.append(linked_dict.get(add_node))
        node_list_one.append(add_node)
        add_node = linked_dict[add_node][-1]
    elif temp <= int(K):
        out_list_two.append(linked_dict.get(add_node))
        node_list_two.append(add_node)
        add_node = linked_dict[add_node][-1]
    else:
        out_list_three.append(linked_dict.get(add_node))
        node_list_three.append(add_node)
        add_node = linked_dict[add_node][-1]

out_list.extend(out_list_one)
out_list.extend(out_list_two)
out_list.extend(out_list_three)
node_list.extend(node_list_one)
node_list.extend(node_list_two)
node_list.extend(node_list_three)
node_list.append('-1')

for i in range(len(out_list)):
    sys.stdout.write('{} {} {}\n'.format(out_list[i][0], out_list[i][1],
                                         node_list[i + 1]))