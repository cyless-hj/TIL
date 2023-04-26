def solution(msg):
    answer = []
    alpha_dict = {chr(65 + i) : i + 1 for i in range(26)}
    
    i = 0
    ch = ''
    num = 27
    while i < len(msg):
        ch += msg[i]
        if ch in alpha_dict:
            i += 1
        else:
            alpha_dict[ch] = num
            num += 1
            answer.append(alpha_dict[ch[:-1]])
            ch = ''
    answer.append(alpha_dict[ch])
    return answer