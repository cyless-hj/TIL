from collections import deque

def solution(order):
    answer = 0
    stack = deque()
    order = deque(order)
    
    for i in range(1, len(order) + 1):
        stack.appendleft(i)
        while stack and stack[0] == order[0]:
            answer += 1
            stack.popleft()
            order.popleft()
    return answer