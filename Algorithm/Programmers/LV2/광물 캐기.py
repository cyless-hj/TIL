from collections import deque

def solution(picks, minerals):
    answer = 0
    tiredList = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    connectionDict = {"diamond": 0, "iron": 1, "stone": 2}
    info = []
    minerals = minerals[:5 * sum(picks)]
    q = deque(minerals)
    while q:
        cnt = 0
        d, i, s = 0, 0, 0
        while cnt < 5:
            cnt += 1
            mineral = q.popleft()
            d += tiredList[0][connectionDict[mineral]]
            i += tiredList[1][connectionDict[mineral]]
            s += tiredList[2][connectionDict[mineral]]
            if not q:
                break
        info.append([d,i,s])
    info.sort(key = lambda x : [x[2],x[1],x[0]])

    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer

    return answer