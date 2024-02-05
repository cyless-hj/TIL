def solution(board, h, w):
    answer = 0
    color = board[h][w]
    length = len(board[0])
    for i in [1, -1]:
        if (0 <= h + i < length):
            if board[h + i][w] == color:
                answer += 1
        if (0 <= w + i < length):
            if board[h][w + i] == color:
                answer += 1
    return answer