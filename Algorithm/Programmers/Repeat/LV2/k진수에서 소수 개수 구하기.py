import string

def solution(n, k):
    def convert(num, base):
        number = string.digits + string.ascii_uppercase
        q, r = divmod(num, base)
        return convert(q, base) + number[r] if q else number[r]
    
    def isPrime(x):
        if x <= 1:
            return False
        for i in range(2, int((x ** (1 / 2)) + 1)):
            if x % i == 0:
                return False
        return True
    
    answer = 0
    conv_num = convert(n, k)
    conv_arr = []
    tmp = ''
    for i in range(len(conv_num)):
        if conv_num[i] != '0':
            tmp += conv_num[i]
        if conv_num[i] == '0' and tmp:
            conv_arr.append(int(tmp))
            tmp = ''
    if tmp:
        conv_arr.append(int(tmp))
    
    for conv in conv_arr:
        if isPrime(conv):
            answer += 1
    return answer