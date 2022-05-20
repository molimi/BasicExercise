"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/20
Description: 统计选择题
"""
import re
import sys
student_count, exercise_count = list(map(int, input().split()))
exercise_list = []
student_list = []
# 读数据
for i in range(exercise_count):
    score, choice_count1, choice_count2, *right_choice = sys.stdin.readline(
    ).split()
    exercise_list.append(
        (int(score), int(choice_count1), int(choice_count2), right_choice))

for j in range(student_count):
    input_list = re.split('[\(\)]', sys.stdin.readline())
    input_list = list(filter(lambda str: str and str.strip(), input_list))
    student_list.append(input_list)

# print(exercise_list)
# print(student_list)
# 统计分析
error_list = [0 for i in range(exercise_count)]
score_list = [0 for i in range(student_count)]
for i in range(student_count):
    for j in range(exercise_count):
        student_choice, *choice3 = list(student_list[i][j])
        choice3 = list(filter(lambda str: str and str.strip(), choice3))
        if int(student_choice) == exercise_list[j][2]:
            if choice3 == exercise_list[j][-1]:
                score_list[i] += exercise_list[j][0]
            else:
                error_list[j] += 1
        else:
            error_list[j] += 1

for k in range(student_count):
    sys.stdout.write('{}\n'.format(score_list[k]))

result_str = ''
if error_list.count(0) == exercise_count:
    print('Too simple')
else:
    max_times = max(error_list)
    result_str = str(max_times)
    for f in range(exercise_count):
        if error_list[f] == max_times:
            result_str += ' ' + str(f + 1)
    print(result_str)