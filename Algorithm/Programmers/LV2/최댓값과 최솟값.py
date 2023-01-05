def solution(s):
    answer = ''
    s = list(map(int, s.split()))
    mx = max(s)
    mn = min(s)
    answer = str(mn) + ' ' + str(mx)
    return answer