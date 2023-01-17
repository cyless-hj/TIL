def solution(want, number, discount):
    answer = 0
    goal_dict = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        tmp_dict = goal_dict.copy()
        for j in range(10):
            tmp_dict[discount[i + j]] = tmp_dict.get(discount[i + j], 0) - 1
            if tmp_dict[discount[i + j]] <= 0:
                del(tmp_dict[discount[i + j]])
        if len(tmp_dict) == 0:
            answer += 1
    return answer