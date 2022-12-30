def solution(numbers):
    answer = -1
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        try:
            n.remove(i)
        except:
            pass
    answer = sum(n)

    return answer