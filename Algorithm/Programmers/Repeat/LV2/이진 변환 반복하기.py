def solution(s):
    cnt, z_cnt = 0, 0
    while True:
        z_cnt += s.count('0')
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]
        cnt += 1
        if s == '1':
            break
    return [cnt, z_cnt]