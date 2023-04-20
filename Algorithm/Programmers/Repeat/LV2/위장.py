def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        dic[cloth[1]] = dic.get(cloth[1], 0) + 1

    for val in dic.values():
        answer *= val + 1
    return answer - 1