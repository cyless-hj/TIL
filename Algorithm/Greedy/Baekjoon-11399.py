import sys

N = int(input())
time = sorted(list(map(int, sys.stdin.readline().split())))

total = 0
tmp = 0

for i in time:
    tmp += i
    total += tmp
    
print(total)