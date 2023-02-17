def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def check(array, g):
    for num in array:
        if num % g == 0:
            return True
    return False

def solution(arrayA, arrayB):
    answer = 0
    gA, gB = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        gA = gcd(gA, arrayA[i])
        gB = gcd(gB, arrayB[i])
    
    if not check(arrayB, gA):
        if gA != 1:
            answer = gA
    
    if not check(arrayA, gB):
        if gB != 1:
            if gB > answer:
                answer = gB
    
    return answer