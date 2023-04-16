def solution(n, arr1, arr2):
    answer = []
    bi1 = []
    bi2 = []
    for i in range(len(arr1)):
        b1 = bin(arr1[i])[2:]
        bi1.append('0' * (n - len(b1)) + b1)
        b2 = bin(arr2[i])[2:]
        bi2.append('0' * (n - len(b2)) + b2)

    bi1 = list(map(lambda x: list(x), bi1))
    bi2 = list(map(lambda x: list(x), bi2))

    for i in range(len(bi1)):
        tmp = ''
        for j in range(len(bi1[0])):
            if bi1[i][j] == '1' or bi2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer