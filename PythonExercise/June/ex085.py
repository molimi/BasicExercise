"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 分数统计
"""


def get_score(id, score):
    if id[0] == 'A':
        result = float(score)
    elif id[0] == 'B':
        result = float(score) / 1.5
    else:
        result = float(score) * 1.5
    return result


def main():
    N = int(input())
    ranking_dict = {}
    for _ in range(N):
        id, score, school = input().split()
        school = school.lower()
        score = get_score(id, score)
        if school in ranking_dict:
            ranking_dict[school][0] += score
            ranking_dict[school][1] += 1
        else:
            ranking_dict[school] = [score, 1]
    ranking_list = sorted(ranking_dict.items(),
                          key=lambda item: (item[1][1], item[0]))
    # 这一步有错，还是先取整再对字典排序
    length = len(ranking_list)
    for k in range(length):
        ranking_list[k][1][0] = int(ranking_list[k][1][0])
    ranking_list.sort(key=lambda item: item[1][0], reverse=True)
    count, flag = 1, 0
    temp_score = ranking_list[0][1][0]
    print(length)
    for j in range(length):
        temp_school, temp_list = ranking_list[j][0], ranking_list[j][1]
        if temp_list[0] == temp_score:
            print('{} {} {} {}'.format(count, temp_school, temp_score,
                                       temp_list[1]))
            flag += 1
        else:
            count += flag
            flag = 1
            temp_score = temp_list[0]
            print('{} {} {} {}'.format(count, temp_school, temp_score,
                                       temp_list[1]))

    # print(ranking_list)


main()