def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if cnt < k:
                if stone - mid <= 0:
                    cnt += 1
                else:
                    cnt = 0
            else:
                break
        if cnt < k:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    return answer