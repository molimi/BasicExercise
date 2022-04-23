"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/15
Description: 分别输出成绩最高和成绩最低的学生
"""


class Student(object):
    def __init__(self, name, number, grade):
        self.name = name
        self.number = number
        self.grade = grade

    def __str__(self):
        return self.name + ' ' + self.number


n = int(input())
student = []
for i in range(n):
    stu_information = input().split(' ')
    student.append(
        Student(stu_information[0], stu_information[1],
                int(stu_information[2])))

student.sort(key=lambda stu: stu.grade)
print(student[-1])
print(student[0])