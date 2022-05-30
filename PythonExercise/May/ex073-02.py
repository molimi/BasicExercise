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
score_list = []  # 每个题目的分数
exercise_list = []  # 习题答案
student_list = []  # 学生答案
choice_list = []  # 正确选项个数
# 读数据

for i in range(exercise_count):  # 选项信息，分数，选项个数，正确选项个数，正确选项
    score, choice_count1, choice_count2, *right_choice = sys.stdin.readline(
    ).split()
    score_list.append(int(score))
    choice_list.append(int(choice_count2))
    exercise_list.append(right_choice)

for j in range(student_count):  # 选项放入列表中，选项个数，选项
    input_list = re.split('[\(\)]', sys.stdin.readline())
    input_list = list(filter(lambda str: str and str.strip(),
                             input_list))  # 去掉空字符串
    student_list.append(input_list)

out_list = [0 for i in range(student_count)]
error_dict = {}
for k in range(student_count):
    for p in range(exercise_count):
        flag = True
        choices_count3, *choices = student_list[k][p].split()
        # choices = list(filter(lambda str: str and str.strip(), choices))
        if choices == exercise_list[p]:
            out_list[k] += score_list[p]
        else:
            for m in range(int(choices_count3)):  # 统计多选的个数
                if choices[m] not in exercise_list[p]:
                    temp_key = str(p + 1) + '-' + choices[m]
                    if temp_key in error_dict:
                        error_dict[temp_key] += 1
                    else:
                        error_dict[temp_key] = 1
                    flag = False
            for n in range(choice_list[p]):  # 漏选的题目数量
                if exercise_list[p][n] not in choices:
                    temp_key = str(p + 1) + '-' + exercise_list[p][n]
                    if temp_key in error_dict:
                        error_dict[temp_key] += 1
                    else:
                        error_dict[temp_key] = 1
            if flag:
                out_list[k] += score_list[p] / 2

for k in range(student_count):
    sys.stdout.write('{:.1f}\n'.format(out_list[k]))

if error_dict:
    max_times = max(error_dict.values())
    result = []
    for k, v in error_dict.items():
        if v == max_times:
            r = result.append((k, v))
    result.sort(key=lambda item: item[0])
    result.sort(key=lambda item: item[1], reverse=True)
    for j in range(len(result)):
        print('{} {}'.format(result[j][1], result[j][0]))
else:
    print('Too simple')