import sys

num = []

for i in range(5):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

print(int(sum(num) / 5))
print(num[2])