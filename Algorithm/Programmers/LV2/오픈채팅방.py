def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        tmp = record[i].split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            dic[tmp[1]] = tmp[2]

    for i in range(len(record)):
        tmp = record[i].split()
        if tmp[0] == 'Enter':
            answer.append(dic[tmp[1]] + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(dic[tmp[1]] + '님이 나갔습니다.')
    return answer