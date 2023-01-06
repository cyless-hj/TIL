def solution(s):
    answer = 0
    arr = []
    for i in s:
        if len(arr) == 0:
            arr.append(i)
        else:
            if i == arr[-1]:
                arr.pop()
            else:
                arr.append(i)
    if len(arr) == 0:
        answer = 1
    else:
        answer = 0
    return answer