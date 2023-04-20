from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        tmp_dic = dic.copy()
        for j in range(10):
            tmp_dic[discount[i + j]] = tmp_dic.get(discount[i + j], 0) - 1
            if tmp_dic[discount[i + j]] <= 0:
                del tmp_dic[discount[i + j]]
        if len(tmp_dic) == 0:
            answer += 1
    return answer