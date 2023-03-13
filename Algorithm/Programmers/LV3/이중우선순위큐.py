import heapq

def solution(operations):
    answer = []
    for oper in operations:
        s = oper.split()
        if s[0] == 'I':
            heapq.heappush(answer, int(s[1]))
        elif len(answer) == 0:
            continue
        elif oper == 'D 1':
            del answer[-1]
        elif oper == 'D -1':
            heapq.heappop(answer)

    answer.sort()
    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [answer[-1], answer[0]]
    return answer