def solution(gems):
    n = len(gems)
    dic = {gems[0]: 1}
    gem_n = len(set(gems))
    answer = [0, n - 1]
    start, end = 0, 0
    
    while start < n and end < n:
        if len(dic) < gem_n:
            end += 1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end - start + 1 < answer[1] - answer[0] + 1:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
            
    answer[0] += 1
    answer[1] += 1
    return answer