import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(data[i][0], data[i][1])