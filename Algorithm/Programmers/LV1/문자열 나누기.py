def solution(s):
    answer = 0
    first_letter = ''
    cnt = 0
    d_cnt = 0
    for i in s:
        if first_letter == '':
            first_letter = i
            cnt += 1
            continue
        
        if i == first_letter:
            cnt += 1
        else:
            d_cnt += 1
        
        if cnt == d_cnt:
            answer += 1
            cnt = 0
            d_cnt = 0
            first_letter = ''
            
    if first_letter:
        answer += 1
    return answer