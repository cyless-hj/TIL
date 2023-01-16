def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        arr = set()
        for i in range(0, len(board) - 1):
            for j in range(0, len(board[0]) - 1):
                if board[i][j] == '0':
                    pass
                elif board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != 0:
                    arr.add((i, j))
                    arr.add((i + 1, j))
                    arr.add((i, j + 1))
                    arr.add((i + 1, j + 1))
        
        if len(arr) == 0:
            break

        for i in arr:
            board[i[0]][i[1]] = 0
            answer += 1
        
        for j in range(len(board[0])):
            tmp_arr = []
            for i in range(len(board)):
                if board[i][j] != 0:
                    tmp_arr.append(board[i][j])
            tmp_arr = [0] * (len(board) - len(tmp_arr)) + tmp_arr
            for k in range(len(board)):
                board[k][j] = tmp_arr[k]

    return answer