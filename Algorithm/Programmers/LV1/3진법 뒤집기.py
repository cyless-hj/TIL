def solution(n):
    answer = 0
    tmp = ''
    
    while n:
        tmp = str(n % 3) + tmp
        n //= 3
    
    tmp = ''.join(reversed(tmp))
    answer = int(tmp, 3)
    return answer