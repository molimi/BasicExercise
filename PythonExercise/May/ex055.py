"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/16
Description: 拍集体照
"""


def sort_list(lst):
    length = len(lst)
    mid = int(length / 2)
    temp_list = ['' for i in range(length)]
    right_index = mid - 1
    left_index = mid + 1
    count = length - 1
    temp_list[mid] = lst[count][0]
    while (right_index >= 0) and (left_index < length):
        count -= 1
        temp_list[right_index] = lst[count][0]
        right_index -= 1
        count -= 1
        temp_list[left_index] = lst[count][0]
        left_index += 1
    if count:
        temp_list[0] = lst[0][0]
    return temp_list


def main():
    N, K = map(int, input().split())
    student_list = []
    for i in range(N):
        name, height = input().split()
        student_list.append((name, int(height)))

    student_list.sort(key=lambda item: item[0], reverse=True)
    student_list.sort(key=lambda item: item[1])
    print(student_list)
    length1 = N // K
    count = 0
    result_list = []
    while True:
        rest = N - count
        if length1 * 2 > rest:
            temp_list = student_list[count:]
            result_list.append(sort_list(temp_list))
            break
        else:
            temp_list = student_list[count:count + length1]
            result_list.append(sort_list(temp_list))
        count += length1

    result_list.reverse()
    for i in range(len(result_list)):
        print(' '.join(map(str, result_list[i])))


main()