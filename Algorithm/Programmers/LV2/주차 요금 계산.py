import math

def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h * 60 + m
    
def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees
    dic = dict()

    for r in records:
        time, number, history = r.split()
        number = int(number)
        
        if number in dic:
            dic[number].append([dateToMinutes(time), history])
        else:
            dic[number] = [[dateToMinutes(time), history]]
    
    rList = list(dic.items())
    rList.sort(key=lambda x : x[0])
    
    for r in rList:
        t = 0
        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer