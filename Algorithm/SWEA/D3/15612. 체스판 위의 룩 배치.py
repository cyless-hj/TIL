T = int(input())
 
for test_case in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    col = []
    row = []
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                row.append(i)
                col.append(j)
                cnt += 1
    if len(set(col))==8 and len(set(row))==8 and cnt == 8:
        print('#{} yes'.format(test_case))
    else:
        print('#{} no'.format(test_case))