"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: 解码PAT注考证
思路一：
第一步，先存储考生信息
第二步，根据命令和指令完成任务
第三步，封装程类
改进，就是用字典吧，好像一个字典还没法解决问题，依然超时，那就三种类别建立三个字典
"""

n, m = map(int, input().split())
type1, type2, type3 = {'B': [], 'A': [], 'T': []}, {}, {}
for i in range(n):
    ID, score = input().split()

    #按类型1分类
    type1[ID[0]].append([ID, int(score)])

    #按类型2分类
    room = ID[1:4]
    if room not in type2:
        type2[room] = [0, 0]
    type2[room][0] += 1
    type2[room][1] += int(score)

    #按类型3分类
    time = ID[4:10]
    if time not in type3:
        type3[time] = {}
    if room not in type3[time]:
        type3[time][room] = 0
    type3[time][room] += 1

for i in range(m):
    style, s = input().split()
    print("Case {0}: {1} {2}".format(i + 1, style, s))

    if style == '1':
        lst = type1[s]
        if len(lst) == 0:
            print("NA")
        else:
            lst.sort(key=lambda x: (-x[1], x[0]))
            for j in range(len(lst)):
                print(lst[j][0], lst[j][1])

    elif style == '2':
        if s not in type2:
            print("NA")
        else:
            lst = type2[s]
            print(lst[0], lst[1])

    elif style == '3':
        if s not in type3:
            print("NA")
        else:
            lst = list(type3[s].items())
            lst.sort(key=lambda x: (-x[1], x[0]))
            for j in range(len(lst)):
                print(lst[j][0], lst[j][1])
