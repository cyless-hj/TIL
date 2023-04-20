def solution(n):
    answer = 0
    a, b = 1, 2
    if n < 3:
        return n
    
    for i in range(1, n - 1):
        a, b = b, a + b
    return b % 1234567