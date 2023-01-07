def solution(today, terms, privacies):
    answer = []
    dic = {}
    today = list(map(int, today.replace('.', ' ').split()))
    for term in terms:
        term = term.split()
        dic[term[0]] = term[1]

    for i in range(len(privacies)):
        privacies[i] = privacies[i].split()
        tmp = list(map(int, privacies[i][0].replace('.', ' ').split()))

        y = today[0] - tmp[0]
        m = today[1] - tmp[1]
        d = today[2] - tmp[2]
        
        result = (y * 12 + m - int(dic[privacies[i][1]])) * 28 + d

        if result >= 0:
            answer.append(i + 1)
    
    return answer