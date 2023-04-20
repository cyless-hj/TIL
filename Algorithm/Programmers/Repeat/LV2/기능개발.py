from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    
    while queue:
        for i in range(len(queue)):
            queue[i] += speeds[i]
            
        count = 0
        while True:
            if not queue:
                answer.append(count)
                break
            if queue[0] >= 100:
                queue.popleft()
                del speeds[0]
                count += 1
            else:
                if count > 0:
                    answer.append(count)
                break
    return answer