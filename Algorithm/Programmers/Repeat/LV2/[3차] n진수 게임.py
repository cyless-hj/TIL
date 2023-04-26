import string

def tenToN(num, base):
        number = string.digits + string.ascii_uppercase
        q, r = divmod(num, base)
        return tenToN(q, base) + number[r] if q else number[r]

def solution(n, t, m, p):
    tmp = ''
    i = 0
    while len(tmp) <= t * m:
        tmp += tenToN(i, n)
        i += 1

    return "".join(tmp[idx] for idx in range(p - 1, t * m, m))