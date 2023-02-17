T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    if n % 2 == 0:
        print('#{} Alice'.format(test_case))
    else:
        print('#{} Bob'.format(test_case))