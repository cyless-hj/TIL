import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_s = sorted(list(set(num)))

dic = {num_s[i] : i for i in range(len(num_s))}

for i in num:
    print(dic[i], end=' ')