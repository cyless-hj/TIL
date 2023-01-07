from collections import deque
def solution(cacheSize, cities):
    answer = 0
    deq = deque()
    cities = list(map(lambda x: x.lower(), cities))
    for i in cities:
        if len(deq) == 0:
            deq.append(i)
            answer += 5
        elif len(deq) == cacheSize:
            if i in deq:
                deq.remove(i)
                deq.append(i)
                answer += 1
            else:
                deq.popleft()
                deq.append(i)
                answer += 5
        else:
            if i in deq:
                deq.remove(i)
                deq.append(i)
                answer += 1
            else:
                deq.append(i)
                answer += 5
    if cacheSize == 0:
        answer = len(cities) * 5
    
    return answer