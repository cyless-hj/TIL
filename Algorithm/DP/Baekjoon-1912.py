import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    n_list[i] = max(n_list[i], n_list[i - 1] + n_list[i])

print(max(n_list))