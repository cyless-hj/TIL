from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    my_doc = [0 for _ in range(len(priorities))]
    my_doc[location] = 1
    my_doc = deque(my_doc)  
    cnt = 0
    while(my_doc): 
        priority = que.popleft()
        check_my_doc = my_doc.popleft()
        if len(que) > 1 and max(que) > priority:
            que.append(priority)
            my_doc.append(check_my_doc)
        else:
            cnt += 1
            if check_my_doc == 1:
                answer = cnt
                break
    return answer