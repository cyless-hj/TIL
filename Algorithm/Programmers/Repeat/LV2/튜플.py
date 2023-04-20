def solution(s):
    answer = []
    s = s.split('},{')
    for i in range(len(s)):
        s[i] = s[i].replace('{', '').replace('}', '')
        s[i] = s[i].split(',')
    s.sort(key=lambda x: len(x))

    for i in range(len(s)):
        for j in range(len(s[i])):
            if int(s[i][j]) not in answer:
                answer.append(int(s[i][j]))
    return answer