def solution(brown, yellow):
    answer = []
    m = (brown / 2 - 2 + (((brown / 2) - 2) **2 - 4 * yellow) ** 0.5) / 2
    n = yellow / m
    return [m + 2, n + 2]
# 2차 방정식 이용(근의 공식)