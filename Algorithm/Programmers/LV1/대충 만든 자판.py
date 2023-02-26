from collections import defaultdict

def solution(keymap, targets):
    answer = []
    dic = defaultdict(int)
    for arr in keymap:
        for s in arr:
            tmp = arr.index(s)
            if dic[s] == 0 or tmp < dic[s]:
                dic[s] = arr.index(s) + 1

    for arr in targets:
        cnt = 0
        for s in arr:
            if dic[s] != 0:
                cnt += dic[s]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer