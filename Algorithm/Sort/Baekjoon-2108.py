import sys
from collections import Counter

num = []
n = int(sys.stdin.readline())
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num) / n))
print(num[n // 2])

num_s = Counter(num).most_common()

if len(num_s) > 1:
    if num_s[0][1] == num_s[1][1]:
        print(num_s[1][0])
    else:
        print(num_s[0][0])
else:
    print(num_s[0][0])
print(num[-1] - num[0])