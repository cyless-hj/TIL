def solution(a, b):
    answer = ''
    tmp = 0
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a == 1:
        answer = week[b % 7 - 1]
    else:
        for i in range(a - 1):
            tmp += month[i]
        tmp += b
        answer = week[tmp % 7 - 1]
    return answer