"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/23
Description: 德才兼备
"""
import sys


def printf(lst):
    # 根据题目要求从大到小输出实际存在的分数
    for i in range(200, 0, -1):
        for j in range(100, 0, -1):
            # 如果当前有值，则通过sorted排序返回一个列表，用for遍历这个排序好的列表依次输出即可
            # 这里存储的是准考证号，要求从小到大
            if lst[i][j]:
                for id in sorted(lst[i][j]):
                    sys.stdout.write('%s %s %s\n' % (id, j, i - j))


def main():
    # 通过列表推导式创建三维列表，为info[][][], 从前往后分别表示总分，德分，准考证号
    first_list = [[[] for j in range(101)] for i in range(201)]
    second_list = [[[] for j in range(101)] for i in range(201)]
    third_list = [[[] for j in range(101)] for i in range(201)]
    fourth_list = [[[] for j in range(101)] for i in range(201)]
    [n, low, high] = list(map(int, input().split()))
    student_list = [
        list(map(int,
                 sys.stdin.readline().split())) for k in range(n)
    ]
    count = n
    for item in student_list:
        # 不满足题目要求的学生不予存入
        if item[1] < low or item[2] < low:
            count -= 1
            continue
        # 由于准考证号值过大，无法通过索引形式，只能append添加至末尾
        elif item[1] >= high and item[2] >= high:
            first_list[item[1] + item[2]][item[1]].append(item[0])
        elif item[1] >= high and item[2] < high:
            second_list[item[1] + item[2]][item[1]].append(item[0])
        elif item[1] >= item[2]:
            third_list[item[1] + item[2]][item[1]].append(item[0])
        else:
            fourth_list[item[1] + item[2]][item[1]].append(item[0])
    print(count)
    printf(first_list)
    printf(second_list)
    printf(third_list)
    printf(fourth_list)


if __name__ == '__main__':
    main()