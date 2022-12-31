import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp1 + tmp2 * 2)
        answer += 1
    return answer