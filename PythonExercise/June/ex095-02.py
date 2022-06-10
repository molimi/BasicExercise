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

import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    student_dict = {}
    for _ in range(N):
        student, grade = sys.stdin.readline().split()
        student_dict[student] = int(grade)
    for j in range(M):
        case, choice = sys.stdin.readline().split()
        out_list = []
        sys.stdout.write('Case {}: {} {}\n'.format(j + 1, case, choice))
        if case == '1':
            for key, value in student_dict.items():
                if key[0] == choice:
                    out_list.append((key, value))
            length = len(out_list)
            if length:
                out_list.sort(key=lambda iter: iter[0])
                out_list.sort(key=lambda iter: iter[1], reverse=True)
                for k in range(length):
                    sys.stdout.write('{} {}\n'.format(out_list[k][0],
                                                      out_list[k][1]))
            else:
                sys.stdout.write('NA\n')
        if case == '2':
            for key, value in student_dict.items():
                if key[1:4] == choice:
                    out_list.append(value)
            length = len(out_list)
            if length:
                sys.stdout.write('{} {}\n'.format(len(out_list),
                                                  sum(out_list)))
            else:
                sys.stdout.write('NA\n')
        if case == '3':
            out_dict = {}
            for key in student_dict:
                temp = key[1:4]
                if key[4:10] == choice:
                    if temp in out_dict:
                        out_dict[temp] += 1
                    else:
                        out_dict[temp] = 1
            length = len(out_dict)
            if length:
                out_list = sorted(out_dict.items(), key=lambda iter: iter[0])
                out_list.sort(key=lambda iter: iter[1], reverse=True)
                for n in range(length):
                    sys.stdout.write('{} {}\n'.format(out_list[n][0],
                                                      out_list[n][1]))
            else:
                sys.stdout.write('NA\n')


main()