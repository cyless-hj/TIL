def solution(arr):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return lcm(arr[0], arr[1])
    else:
        tmp = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            tmp = lcm(tmp, arr[i])
        return tmp