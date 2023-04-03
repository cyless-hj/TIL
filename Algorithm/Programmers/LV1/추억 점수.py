def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for pho in photo:
        cnt = 0
        for p in pho:
            cnt += dic.get(p, 0)
        answer.append(cnt)
    return answer