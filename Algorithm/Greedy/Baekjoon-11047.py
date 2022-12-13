n, k = map(int, input().split())
coin_lst = list()
for i in range(n):
    coin_lst.append(int(input()))

count = 0

for i in reversed(range(n)):
    count += k // coin_lst[i]
    k = k % coin_lst[i]

print(count)