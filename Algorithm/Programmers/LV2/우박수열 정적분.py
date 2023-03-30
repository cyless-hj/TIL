def solution(k, ranges):
    answer = []
    tmp = [[0, k]]
    area = []
    idx = 1
    while k != 1:
        if k % 2 == 0:
            k //= 2
            tmp.append([idx, k])
        else:
            k = k * 3 + 1
            tmp.append([idx, k])
        area.append((tmp[idx - 1][1] + k) / 2)
        idx += 1

    for ran in ranges:
        if ran == [0, 0]:
            answer.append(sum(area))
        else:
            if ran[0] - ran[1] > idx - 1:
                answer.append(-1.0)
            elif ran[0] - ran[1] == idx - 1:
                answer.append(0.0)
            else:
                answer.append(sum(area[ran[0]:idx + ran[1] - 1]))
    return answer