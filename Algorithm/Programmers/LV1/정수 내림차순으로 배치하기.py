def solution(n):
    stn = str(n)
    li = []
    for i in range(len(stn)):
        li.append(int(stn[i]))
        
    li.sort(reverse = True)
    
    for i in range(len(li)):
        li[i] = str(li[i])
    
    answer = int(''.join(li))
    return answer