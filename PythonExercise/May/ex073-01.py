"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/25
Description: 多选题计算分数
思路：
一、首先是输入怎么获得自己想要的格式，可以使用正则表达式，或者使用字符串的replace和split
二、判断选项是否全对，并统计每位学生的分数
三、判断多选的错误选项数目，两种情况，一种是多选了，另一种是少选了
"""

import re
import sys
student_count, exercise_count = list(map(int, input().split()))
exercise_list = []
student_list = []
# 读数据
for i in range(exercise_count):  # 选项信息,分数，选项个数，正确选项个数，正确选项
    score, choice_count1, choice_count2, *right_choice = sys.stdin.readline(
    ).split()
    exercise_list.append(
        (int(score), int(choice_count1), int(choice_count2), right_choice))

for j in range(student_count):  # 选项放入列表中，选项个数，选项
    input_list = re.split('[\(\)]', sys.stdin.readline())
    input_list = list(filter(lambda str: str and str.strip(),
                             input_list))  # 去掉空字符串
    student_list.append(input_list)

# print(exercise_list)
# print(student_list)
# 统计分析
error_list = [0 for i in range(exercise_count)]
score_list = [0 for i in range(student_count)]
choice_dict = {}
for i in range(student_count):
    for j in range(exercise_count):
        student_choice, *choice3 = list(student_list[i][j])  # 学生选项个数和选项
        choice3 = list(filter(lambda str: str and str.strip(), choice3))
        if choice3 == exercise_list[j][-1]:
            score_list[i] += exercise_list[j][0]
        elif set(choice3).issubset(exercise_list[j][-1]):
            score_list[i] += exercise_list[j][0] / 2
            for m in range(exercise_list[j][2]):  # 统计少选的选项
                if exercise_list[j][-1][m] not in choice3:
                    if j in choice_dict:
                        if exercise_list[j][-1][m] in choice_dict[j]:
                            choice_dict[j][exercise_list[j][-1][m]] += 1
                        else:
                            choice_dict[j][exercise_list[j][-1][m]] = 1
                    else:
                        choice_dict[j] = {}
                        choice_dict[j][exercise_list[j][-1][m]] = 1

        else:
            error_list[j] += 1
            for k in range(int(student_choice)):  # 统计选错的次数
                if choice3[k] not in exercise_list[j][-1]:
                    if j in choice_dict:
                        if choice3[k] in choice_dict[j]:
                            choice_dict[j][choice3[k]] += 1
                        else:
                            choice_dict[j][choice3[k]] = 1
                    else:
                        choice_dict[j] = {}
                        choice_dict[j][choice3[k]] = 1
            for m in range(exercise_list[j][2]):  # 统计漏选的次数
                if exercise_list[j][-1][m] not in choice3:
                    if j in choice_dict:
                        if exercise_list[j][-1][m] in choice_dict[j]:
                            choice_dict[j][exercise_list[j][-1][m]] += 1
                        else:
                            choice_dict[j][exercise_list[j][-1][m]] = 1
                    else:
                        choice_dict[j] = {}
                        choice_dict[j][exercise_list[j][-1][m]] = 1

for k in range(student_count):
    sys.stdout.write('{:.1f}\n'.format(score_list[k]))

result_str = ''
if error_list.count(0) == exercise_count:
    print('Too simple')
else:
    max_times = max(error_list)
    for f in range(exercise_count):
        if error_list[f] == max_times:
            choice_list = sorted(choice_dict[f].items(),
                                 key=lambda item: item[1])
            # print(choice_list)
            max_choice = choice_list[-1][1]
            for m in range(len(choice_list)):
                result_str = str(max_times)
                if choice_list[m][1] == max_choice:
                    result_str += ' ' + str(f + 1) + '-' + choice_list[m][0]
                    print(result_str)