import string
def tenToN(n, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(n, base)
    return tenToN(q, base) + number[r] if q else number[r]

def solution(n, t, m, p):
    answer = ''
    s = ''
    i = 0
    while len(s) <= t * m:
        s += tenToN(i, n)
        i += 1
    print(s)

    answer = "".join(s[idx] for idx in range(p - 1, t * m, m))
    return answer