import sys
from collections import deque

n = int(sys.stdin.readline())

card = deque(list(range(1, n + 1)))

while True:
    if n != 1:
        card.popleft()
        card.append(card.popleft())
    if len(card) == 1:
        answer = card.pop()
        break
print(answer)