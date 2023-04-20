def solution(s):
    answer = -1

    stack = []
    for st in s:
        if not stack:
            stack.append(st)
        else:
            if stack[-1] == st:
                stack.pop()
            else:
                stack.append(st)
    if stack:
        return 0

    return 1