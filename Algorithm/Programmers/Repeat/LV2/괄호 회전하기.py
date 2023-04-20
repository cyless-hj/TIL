def solution(s):
    answer = 0
    
    def corect(s):
        stack = []
        for st in s:
            if not stack:
                stack.append(st)
            else:
                if (stack[-1] == '(' and st == ')') or (stack[-1] == '{' and st == '}') or (stack[-1] == '[' and st == ']'):
                    stack.pop()
                else:
                    stack.append(st)
        if stack:
            return False
        return True
    
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if corect(tmp):
            answer += 1
    return answer