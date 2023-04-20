from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    idx_arr = deque([0 if x != location else 1 for x in range(len(priorities))])
    
    while idx_arr:
        priority = priorities.popleft()
        idx = idx_arr.popleft()
        
        if len(priorities) > 1 and max(priorities) > priority:
            priorities.append(priority)
            idx_arr.append(idx)
        else:
            answer += 1
            if idx == 1:
                return answer