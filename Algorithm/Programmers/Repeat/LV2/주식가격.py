from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        cnt = 0
        price = prices.popleft()
        for p in prices:
            cnt += 1
            if p < price:
                break
        answer.append(cnt)
                
    return answer