"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/23
Description: 德才兼备
"""
'''
# 笨办法排序实现
def sort_list(out_list):
    put_list = out_list[:]
    length = len(put_list)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if put_list[j][1] + put_list[j][2] < put_list[j + 1][1] + put_list[
                    j + 1][2]:
                put_list[j], put_list[j + 1] = put_list[j + 1], put_list[j]
                swapped = True
            elif put_list[j][1] + put_list[j][2] == put_list[
                    j + 1][1] + put_list[j + 1][2]:
                if put_list[j][1] < put_list[j + 1][1]:
                    put_list[j], put_list[j + 1] = put_list[j + 1], put_list[j]
                elif put_list[j][1] == put_list[j + 1][1]:
                    if put_list[j][0] > put_list[j + 1][0]:
                        put_list[j], put_list[j + 1] = put_list[j +
                                                                1], put_list[j]
                swapped = True
        if not swapped:
            break
    return put_list
'''
[n, low, high] = list(map(int, input().split()))
first_list = []
second_list = []
third_list = []
fourth_list = []
count = n
for i in range(n):
    items = list(map(int, input().split()))
    if items[1] < low or items[2] < low:
        count -= 1
        continue
    elif items[1] >= high and items[2] >= high:
        first_list.append(items)
    elif items[1] >= high and items[2] < high:
        second_list.append(items)
    elif items[1] >= items[2]:
        third_list.append(items)
    else:
        fourth_list.append(items)

key = lambda item: (item[1] + item[2], item[1], -item[0])
first_list.sort(key=key, reverse=True)
second_list.sort(key=key, reverse=True)
third_list.sort(key=key, reverse=True)
fourth_list.sort(key=key, reverse=True)
result_list = first_list + second_list + third_list + fourth_list

print(count)
for k in range(count - 1):
    print('{} {} {}'.format(result_list[k][0], result_list[k][1],
                            result_list[k][2]))
print('{} {} {}'.format(result_list[-1][0], result_list[-1][1],
                        result_list[-1][2]),
      end='')