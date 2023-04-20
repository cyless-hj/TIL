def solution(n):
    answer = 0
    n_cnt = str(bin(n)[2:]).count('1')
    nxt = n + 1
    while True:
        nxt_cnt = str(bin(nxt)[2:]).count('1')
        if n_cnt == nxt_cnt:
            return nxt
        else:
            nxt += 1