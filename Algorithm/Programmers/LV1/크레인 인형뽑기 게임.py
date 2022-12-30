def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0: # -1로 인덱스
                if len(stack) == 0:
                    stack.append(board[j][i - 1])

                else:
                    if board[j][i - 1] == stack[-1]:
                        answer += 2 # 2개씩 지워짐
                        stack.pop()

                    else:
                        stack.append(board[j][i - 1])

                board[j][i - 1] = 0 # 처리 후 빈칸으로 만들기
                break # 처리 후 반복을 나와야한다.

    return answer