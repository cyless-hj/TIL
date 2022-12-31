# from collections import Counter

# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]

def solution(participant, completion):
    dic = {}
    for part in participant:
    	dic[part] = dic.get(part,  0) + 1

    for com in completion:
    	dic[com] -= 1

    dnf = [k for k, v in dic.items() if v > 0]
    answer = dnf[0]
    return answer