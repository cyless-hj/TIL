from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    L = sum(queue1)
    R = sum(queue2)
    
    goal = (sum(queue1) + sum(queue2))
    if goal % 2 != 0:
        return -1
    
    while True:
        if L < R:
            tmp = queue2.popleft()
            queue1.append(tmp)
            L += tmp
            R -= tmp
            answer += 1
        elif L > R:
            tmp = queue1.popleft()
            queue2.append(tmp)
            L -= tmp
            R += tmp
            answer += 1
        else:
            break

        if answer == len(queue1) * 4:
            answer = -1
            break
    return answer