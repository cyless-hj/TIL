from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    tmp1 = cards1.popleft()
    tmp2 = cards2.popleft()
    
    while goal:
        target = goal.popleft()
        if target == tmp1:
            if len(cards1) != 0:
                tmp1 = cards1.popleft()
        elif target == tmp2:
            if len(cards2) != 0:
                tmp2 = cards2.popleft()
        else:
            answer = 'No'
    return answer