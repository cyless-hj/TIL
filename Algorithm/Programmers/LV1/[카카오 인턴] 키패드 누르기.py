def solution(numbers, hand):
    answer = ''
    pad = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]
    rc = 11
    lc = 10
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            lc = num
        elif num in [3, 6, 9]:
            answer += 'R'
            rc = num
        else:
            ld = abs(pad[lc][0] - pad[num][0]) + abs(pad[lc][1] - pad[num][1])
            rd = abs(pad[rc][0] - pad[num][0]) + abs(pad[rc][1] - pad[num][1])
            if ld > rd:
                answer += 'R'
                rc = num
            elif ld < rd:
                answer += 'L'
                lc = num
            else:
                if hand == 'right':
                    answer += 'R'
                    rc = num
                else:
                    answer += 'L'
                    lc = num
    return answer