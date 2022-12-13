import sys

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(H)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for i in H:
        if i > mid:
            total += i - mid
    
    if total < M:
        end = mid - 1
    
    else:
        start = mid + 1

print(end)