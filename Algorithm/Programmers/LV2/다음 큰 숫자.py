from collections import Counter

def solution(n):
    answer = 0
    binary_n = bin(n)[2:]
    n_cnt = Counter(binary_n)['1']
    while True:
        n += 1
        binary_next = bin(n)[2:]
        next_cnt = Counter(binary_next)['1']
        if n_cnt == next_cnt:
            answer = n
            break
    return answer