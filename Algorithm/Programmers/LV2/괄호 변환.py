def divide(p):
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]

def correct(u):
    stack = []
    
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ""
    
    u, v = divide(p)
    
    if correct(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        
        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer