from collections import deque

def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    remain = deque()
    cnt = 1
    for i in range(len(pro)):
        if (100 - pro[i]) % speeds[i] != 0:
            remain.append((100 - pro[i]) // speeds[i] + 1)
        else:
            remain.append((100 - pro[i]) // speeds[i])
            
    for i in range(len(remain)):
        if i == 0:
            tmp = remain.popleft()
        else:
            tmp2 = remain.popleft()
            if tmp >= tmp2:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                tmp = tmp2
    answer.append(cnt)
        
    
    return answer