import string

def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    alpha = [x for x in list(string.ascii_lowercase) if x not in skip]
    len_a = len(alpha)
    for i in s:
        answer += alpha[(alpha.index(i) + index) % len_a]
    return answer