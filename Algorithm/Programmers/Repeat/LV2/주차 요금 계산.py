import math

def solution(fees, records):
    answer = []
    dic = {}
    base_time, base_fee, extend_time, extend_fee = fees
    records = list(map(lambda x: x.split(), records))
    
    for record in records:
        h, m = record[0].split(':')
        if int(record[1]) in dic:
            dic[int(record[1])].append([int(h) * 60 + int(m), record[2]])
        else:
            dic[int(record[1])] = [[int(h) * 60 + int(m), record[2]]]
    
    record_arr = sorted(list(dic.items()), key=lambda x: x[0])
    
    for record in record_arr:
        time = 0
        for info in record[1]:
            if info[1] == "IN":
                time -= info[0]
            else:
                time += info[0]

        if record[1][-1][1] == "IN":
            time += 23 * 60 + 59
        if time <= base_time:
            answer.append(base_fee)
        else:
            answer.append(base_fee + math.ceil((time - base_time) / extend_time) * extend_fee)        

    return answer