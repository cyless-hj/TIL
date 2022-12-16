import sys

s = str(sys.stdin.readline())
alphabet = list(range(97,123))

for x in alphabet :
    print(s.find(chr(x)))