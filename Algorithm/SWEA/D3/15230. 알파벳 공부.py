import string

T = int(input())

for test_case in range(1, T + 1):
    s = input()
    answer = 0
    alpha = string.ascii_lowercase
    for i in range(len(s)):
        if s[i] == alpha[i]:
            answer += 1
        else:
            break
    print('#{} {}'.format(test_case, answer))