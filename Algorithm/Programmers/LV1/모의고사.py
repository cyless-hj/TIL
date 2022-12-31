def solution(answers):
    answer = []
    score = [0, 0, 0]
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    for idx, ans in enumerate(answers):
        if ans == man1[idx % len(man1)]:
            score[0] += 1
        if ans == man2[idx % len(man2)]:
            score[1] += 1
        if ans == man3[idx % len(man3)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)
    return answer