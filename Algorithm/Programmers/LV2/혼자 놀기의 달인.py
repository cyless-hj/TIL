def solution(cards):
    answer = 0
    check = []
    len_list = []
    for i in range(len(cards)):
        box = []
        tmp = i
        while True:
            if cards[tmp] not in check:
                check.append(cards[tmp])
                box.append(cards[tmp])
                tmp = cards[tmp] - 1
            else:
                len_list.append(len(box))
                break
        
        if len(check) == len(cards):
            break
    
    len_list.sort(reverse=True)
    
    if len(len_list) == 1:
        answer = 0
    else:
        answer = len_list[0] * len_list[1]
    return answer