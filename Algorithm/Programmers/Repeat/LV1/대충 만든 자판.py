def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for j in range(len(key)):
            tmp = dic.get(key[j], 101)
            if j + 1 < tmp:
                dic[key[j]] = j + 1
    for target in targets:
        cnt = 0
        for j in range(len(target)):
            if target[j] in dic.keys():
                cnt += dic[target[j]]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer