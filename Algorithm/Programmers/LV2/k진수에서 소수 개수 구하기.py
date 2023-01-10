from collections import deque

def solution(n, k):
    answer = 0

    def convert(num, base):
        number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        q, r = divmod(num, base)
        return convert(q, base) + number[r] if q else number[r]
    
    def isPrime(x):
        for i in range(2, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                return False
        return True
    
    con = convert(n, k)

    for n in con.split('0'):
        if n == "" or n == '1':
            continue
        if isPrime(int(n)):
            answer += 1
    return answer