import sys

num = []

n = int(sys.stdin.readline())

for i in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

for i in range(n):
    print(num[i])