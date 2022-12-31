def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    tmp = sorted(numbers, key = lambda x: x * 3, reverse=True)
    answer += str(int(''.join(tmp)))
    return answer