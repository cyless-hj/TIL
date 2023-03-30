from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    enemyMoong = []

    for enemyNow in enemy:
        heappush(enemyMoong, -enemyNow)   

        if n >= enemyNow:
            n -= enemyNow
            answer += 1            
        else:
            if k :
                n += -heappop(enemyMoong) - enemyNow
                k -= 1
                answer += 1
            else:
                break
    return answer