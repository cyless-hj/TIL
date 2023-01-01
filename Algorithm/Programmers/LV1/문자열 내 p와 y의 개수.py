def solution(s):
    answer = True
    s = s.lower()
    pnt = 0
    ynt = 0
    for i in s:
        if i == 'p':
            pnt += 1
        elif i == 'y':
            ynt += 1
    if pnt != ynt:
        answer = False
    return answer