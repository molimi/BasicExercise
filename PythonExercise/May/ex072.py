"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/25
Description: 开学寄语
"""
N, K = list(map(int, input().split()))
find_list = input().split()
out_list = []
for i in range(N):
    temp_dict = {}  # 用字典更有利于输出
    name, number, *index = input().split()
    for j in range(int(number)):
        if index[j] in find_list:
            if name in temp_dict:
                temp_dict[name].append(index[j])
            else:
                temp_dict[name] = []
                temp_dict[name].append(index[j])
    if temp_dict:
        out_list.append(temp_dict)

length = len(out_list)
count = 0

print(out_list)
for k in range(length):
    keys = list(out_list[k].keys())
    values = list(out_list[k].values())[0]
    count += len(values)
    result = ' '.join(keys) + ': ' + ' '.join(values)
    print(result)
print('{} {}'.format(length, count))