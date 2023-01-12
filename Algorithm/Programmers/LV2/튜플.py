def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    for i in range(len(s)):
        s[i] = set(s[i].split(','))
    s = sorted(s, key=lambda x: len(x))

    answer.append(int(list(s[0])[0]))
    for i in range(1, len(s)):
        answer.append(int(list(s[i] - s[i - 1])[0]))
    print(answer)
    return answer