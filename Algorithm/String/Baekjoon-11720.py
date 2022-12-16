import sys

n = int(sys.stdin.readline())
num = str(sys.stdin.readline())

sum = 0

for i in range(n):
    sum += int(num[i])

print(sum)