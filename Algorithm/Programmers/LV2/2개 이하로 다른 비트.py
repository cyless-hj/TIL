def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            str_num = bin(num)[2:]
            num_list = list(str_num)
            
            if '0' in num_list:
                for i in range(len(num_list) - 1, -1, -1):
                    if num_list[i] == '0':
                        num_list[i] = '1'
                        num_list[i + 1] = '0'
                        break
            else:
                num_list = list('1' + str_num)
                num_list[1] = '0'
                
            num = ''.join(num_list)
            answer.append(int(''.join(num), 2))
            
    return answer