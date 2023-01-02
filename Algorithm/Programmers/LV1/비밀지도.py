def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr1[i] = list('0' * (n - len(bin(arr1[i])[2:])) + bin(arr1[i])[2:])
        arr2[i] = list('0' * (n - len(bin(arr2[i])[2:])) + bin(arr2[i])[2:])
        for j in range(len(arr1[i])):
            if arr1[i][j] != arr2[i][j]:
                arr1[i][j] = '#'
            elif arr1[i][j] == arr2[i][j]:
                if arr1[i][j] == '0':
                    arr1[i][j] = ' '
                else:
                    arr1[i][j] = '#'
        arr1[i] = ''.join(arr1[i])
    
    return arr1