def solution(plans):
    answer = []
    stack = []
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
    
    while plans:
        sub, start, remain = plans.pop()
        if stack:
            pre_sub, pre_start, pre_remain = stack.pop()
            term = start - pre_start
            if term < pre_remain:
                stack.append((pre_sub, pre_start, pre_remain - term))
            else:
                answer.append(pre_sub)
                term = term - pre_remain

                while stack and term:
                    pre_sub, pre_start, pre_remain = stack.pop()

                    if term < pre_remain:
                        stack.append((pre_sub, pre_start, pre_remain - term))
                        break
                    else:
                        answer.append(pre_sub)
                        term = term - pre_remain
        stack.append((sub, start, remain))

    answer.extend([sub for sub, st, ti in stack[::-1]])
    return answer