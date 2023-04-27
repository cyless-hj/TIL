def solution(record):
    answer = []
    dic = {}
    for rec in record:
        rec_arr = rec.split()
        if rec_arr[0] == 'Enter' or rec_arr[0] == 'Change':
            dic[rec_arr[1]] = rec_arr[2]
    
    for rec in record:
        rec_arr = rec.split()
        if rec_arr[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[rec_arr[1]]))
        elif rec_arr[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(dic[rec_arr[1]]))
    return answer