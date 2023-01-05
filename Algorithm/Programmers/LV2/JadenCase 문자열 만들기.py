def solution(s):
    answer = ''
    s_list = list(s)
    
    if s_list[0].isalpha():
        s_list[0] = s_list[0].upper()
    
    for i in range(1, len(s_list)):
        if s_list[i - 1] == ' ' and s_list[i].isalpha():
            s_list[i] = s_list[i].upper()
        elif s_list[i - 1] != ' ' and s_list[i].isalpha():
            s_list[i] = s_list[i].lower()

    answer = ''.join(s_list)
    return answer