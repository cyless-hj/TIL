def solution(lottos, win_nums):
    answer = []
    cnt = 0
    znt = 0
    for i in lottos:
        if i == 0:
            znt += 1
            continue
        for j in win_nums:
            if i == j:
                cnt += 1
    snt = cnt + znt
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = [rank[snt],rank[cnt]]
    return answer