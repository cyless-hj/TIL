def solution(n, words):
    answer = []
    cnt = 0
    stack = []

    for i in range(len(words)):
        num = i % n + 1
        if i % n == 0:
            cnt += 1
        if i == 0:
            stack.append(words[i])
        else:
            if words[i] in stack:
                answer.append(num)
                answer.append(cnt)
                break
            else:
                if stack[-1][-1] == words[i][0]:
                    stack.append(words[i])
                elif stack[-1][-1] != words[i][0]:
                    answer.append(num)
                    answer.append(cnt)
                    break
    if len(answer) == 0:
        answer = [0, 0]

    return answer