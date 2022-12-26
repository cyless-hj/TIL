import sys

a, b = map(str, sys.stdin.readline().split())

a, b = "".join(reversed(a)), "".join(reversed(b))
a, b = int(a), int(b)

print(max(a, b))