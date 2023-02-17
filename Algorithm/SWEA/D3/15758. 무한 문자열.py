T = int(input())

for test_case in range(1, T + 1):
    s1, s2 = input().split()
    s1_l = len(s1)
    s2_l = len(s2)
    
    if s1 * s2_l == s2 * s1_l:
        print('#{} yes'.format(test_case))
    else:
        print('#{} no'.format(test_case))