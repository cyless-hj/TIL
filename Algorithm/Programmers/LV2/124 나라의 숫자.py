def tenToN(n):
    number = '124'
    q, r = divmod(n, 3)
    if n % 3 == 0:
        q = q - 1
    return tenToN(q) + number[r - 1] if q else number[r - 1]

def solution(n):
    answer = tenToN(n)
    return answer