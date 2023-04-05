from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        info_tmp = info[i].split()
        key = info_tmp[:-1]
        value = info_tmp[-1]
        
        for j in range(5):
            for comb in combinations(key, j):
                tmp = ''.join(comb)
                if tmp in info_dict:
                    info_dict[tmp].append(int(value))
                else:
                    info_dict[tmp] = [int(value)]
    for i in info_dict:
        info_dict[i].sort()
    
    for q in query:
        q_tmp = q.split()
        q_key = q_tmp[:-1]
        q_value = q_tmp[-1]
        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')
            
        q_key = ''.join(q_key)
        
        if q_key in info_dict:
            scores = info_dict[q_key]

            if scores:
                enter = bisect_left(scores, int(q_value))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    return answer