import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort(reverse=True)

print(num[k - 1])