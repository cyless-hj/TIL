from collections import deque

def solution(input_string):
    answer = ''
    answer_list = []
    dic = {}
    for idx, alpha in enumerate(input_string):
        if alpha not in dic:
            dic[alpha] = [idx]
        else:
            dic[alpha].append(idx)
    for key, value in dic.items():
        if len(value) >= 2:
            for i in range(len(value) - 1):
                if abs(value[i] - value[i + 1]) > 1:
                    answer_list.append(key)
                    break

    answer = ''.join(sorted(answer_list))
    if not answer:
        return 'N'
    return answer