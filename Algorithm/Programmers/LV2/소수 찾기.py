from itertools import permutations

def isPrime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    permute = set()
    arr = []
    for i in range(1, len(numbers) + 1):
        permute |= set(permutations(list(numbers), i))

    for i in permute:
        if int(''.join(i)) != 0 and int(''.join(i)) != 1:
            arr.append(int(''.join(i)))

    for num in set(arr):
        if isPrime(num):
            answer += 1
    return answer