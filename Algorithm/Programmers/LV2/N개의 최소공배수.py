from math import gcd
from collections import deque

def solution(arr):
    answer = 0
    arr = deque(arr)
    while len(arr) != 1:
        a = arr.popleft()
        b = arr.popleft()
        arr.append(a * b // gcd(a, b))
        answer = arr[-1]
    
    return answer