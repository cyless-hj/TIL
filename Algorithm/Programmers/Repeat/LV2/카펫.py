def solution(brown, yellow):
    answer = []
    m = (brown / 2 - 2 + (((brown / 2) - 2) **2 - 4 * yellow) ** 0.5) / 2
    n = yellow / m
    return [m + 2, n + 2]