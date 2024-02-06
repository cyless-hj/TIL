def solution(bandage, health, attacks):
    answer = health
    for i in range(len(attacks)):
        if i == 0:
            answer += (attacks[i][0] - 1) * bandage[1] + (attacks[i][0] - 1) // bandage[0] * bandage[2]
            if answer > health:
                answer = health
            answer -= attacks[i][1]
        else:
            answer += (attacks[i][0] - attacks[i - 1][0] - 1) * bandage[1] + (attacks[i][0] - attacks[i - 1][0] - 1) // bandage[0] * bandage[2]
            if answer > health:
                answer = health
            answer -= attacks[i][1]
        if answer <= 0:
            return -1
    return answer