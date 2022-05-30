"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/28
Description: 成绩互评
最后四舍五入，
技巧一：+0.5取整
技巧二：
from decimal import Decimal
Decimal('50.5679').quantize(Decimal('0.00'))
小坑：round(1.5)=2, round(2.5)=2
"""
N, M = input().split()
for i in range(int(N)):
    teacher_score, *student_score = list(map(int, input().split()))
    student_list = list(filter(lambda iter: 0 <= iter <= int(M),
                               student_score))
    student_list.remove(max(student_list))
    student_list.remove(min(student_list))
    score = (teacher_score + sum(student_list) / len(student_list)) / 2 + 0.5
    print(int(score))