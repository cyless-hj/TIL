def solution(x):
    answer = True
    num = 0
    s = str(x)
    for i in s:
        num += int(i)
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer