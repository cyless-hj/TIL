import sys

n = int(sys.stdin.readline())
for i in range(n):
    num, s = sys.stdin.readline().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)