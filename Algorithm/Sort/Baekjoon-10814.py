import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(str, sys.stdin.readline().split())))
data.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(data[i][0], data[i][1])