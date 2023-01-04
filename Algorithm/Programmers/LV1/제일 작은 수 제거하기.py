def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
    answer = arr
    return answer