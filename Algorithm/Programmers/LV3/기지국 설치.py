def solution(n, stations, w):
    answer = 0
    no = []
    tmp = 1
    gizi = 2 * w + 1
    if stations[0] - w - 1 >= 1:
        no.append([1, stations[0] - w - 1])
        
    for i in range(len(stations) - 1):
        start = stations[i] + w + 1
        end = stations[i + 1] - w - 1
        if start <= end:
            no.append([start, end])
            
    if stations[-1] + w + 1 <= n:
        no.append([stations[-1] + w + 1, n])

    for dis in no:
        tmp = dis[1] - dis[0] + 1
        q, r = divmod(tmp, gizi)
        if r:
            answer += q + 1
        else:
            answer += q
    return answer