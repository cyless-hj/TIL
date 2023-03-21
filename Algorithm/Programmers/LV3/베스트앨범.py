def solution(genres, plays):
    answer = []
    dic = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic.keys():
            dic[genre] = dic[genre][0] + play, dic[genre][1] + [[play, i]]
        else:
            dic[genre] = [play, [[play, i]]]
    
    for _, indexs in sorted(dic.items(), key=lambda x: -x[1][0]):
        for index in sorted(indexs[1], key=lambda x: -x[0])[:2]:
            answer.append(index[1])

    return answer