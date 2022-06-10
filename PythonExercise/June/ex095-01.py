"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: 解码PAT注考证
思路一：
第一步，先存储考生信息
第二步，根据命令和指令完成任务
第三步，封装程类
问题：难道说使用类增加了问题复杂性，所以超时了
"""

import sys


class StudentInformation(object):
    """
    :param level: 考试级别
    :param exam_number: 考试编号
    :param date: 日期
    :param student_number: 考生编号
    :param grade: 成绩
    """
    def __init__(self, level, exam_number, date, student_number, grade):
        self.level = level
        self.exam_number = exam_number
        self.date = date
        self.student_number = student_number
        self.grade = grade

    def join(self):
        return (self.level + self.exam_number + self.date +
                self.student_number, self.grade)


def main():
    N, M = map(int, sys.stdin.readline().split())
    student_list = []
    for _ in range(N):
        student, grade = sys.stdin.readline().split()
        student_list.append(
            StudentInformation(student[0], student[1:4], student[4:10],
                               student[10:], int(grade)))
    student_set = set(student_list)
    for j in range(M):
        case, choice = sys.stdin.readline().split()
        out_list = []
        print('Case {}: {} {}'.format(j + 1, case, choice))
        if case == '1':
            for item in student_set:
                if item.level == choice:
                    out_list.append(item.join())
            length = len(out_list)
            if length:
                out_list.sort(key=lambda iter: iter[0])
                out_list.sort(key=lambda iter: iter[1], reverse=True)
                for k in range(length):
                    print('{} {}'.format(out_list[k][0], out_list[k][1]))
            else:
                print('NA')
        if case == '2':
            for item in student_set:
                if item.exam_number == choice:
                    out_list.append(item.grade)
            length = len(out_list)
            if length:
                print('{} {}'.format(len(out_list), sum(out_list)))
            else:
                print('NA')
        if case == '3':
            out_dict = {}
            for item in student_set:
                if item.date == choice:
                    if item.exam_number in out_dict:
                        out_dict[item.exam_number] += 1
                    else:
                        out_dict[item.exam_number] = 1
            length = len(out_dict)
            if length:
                out_list = sorted(out_dict.items(), key=lambda iter: iter[0])
                out_list.sort(key=lambda iter: iter[1], reverse=True)
                for n in range(length):
                    print('{} {}'.format(out_list[n][0], out_list[n][1]))
            else:
                print('NA')


main()