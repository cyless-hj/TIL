def solution(survey, choices):
    answer = ''
    dic = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    add_score = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}
    for i in range(len(survey)):
        dic[survey[i][0]] += add_score[choices[i]]
    
    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += "C" if dic["C"] >= dic["F"] else "F"
    answer += "J" if dic["J"] >= dic["M"] else "M"
    answer += "A" if dic["A"] >= dic["N"] else "N"
    return answer