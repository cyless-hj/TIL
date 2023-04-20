def solution(s):
    stack = []
    for st in s:
        if not stack:
            stack.append(st)
        else:
            if st == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(st)
    if stack:
        return False
    return True