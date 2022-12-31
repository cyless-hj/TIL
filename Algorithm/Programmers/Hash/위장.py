def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = dic.get(i[1],  0) + 1
    for key in dic.keys():
        answer *= (dic[key] + 1)
    return answer - 1