import sys

n = int(input())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

m_cost = cost[0]
total = 0

for i in range(n - 1):
    if m_cost > cost[i]:
        m_cost = cost[i]
    total += m_cost * dist[i]

print(total)