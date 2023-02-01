def generate_matrix(rows, columns):
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i - 1][j - 1] = columns * (i - 1) + j
    return matrix

def change(x1, y1, x2, y2, matrix):
    min_value = 10001
    # 맨 위의 맨 왼쪽 값을 기록
    temp = matrix[x1][y1]
    # 왼쪽
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k + 1][y1]
        min_value = min(min_value, matrix[k + 1][y1])
    # 아래
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k + 1]
        min_value = min(min_value, matrix[x2][k + 1])
    # 오른쪽
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k - 1][y2]
        min_value = min(min_value, matrix[k - 1][y2])
    # 위
    for k in range(y2, y1 + 1, -1):
        matrix[x1][k] = matrix[x1][k - 1]
        min_value = min(min_value, matrix[x1][k - 1])
    # 기록했던 값 업데이트
    matrix[x1][y1 + 1] = temp
    min_value = min(min_value, temp)
    return min_value

def solution(rows, columns, queries):
    answer = []
    matrix = generate_matrix(rows, columns)
    for x1, y1, x2, y2 in queries:
        answer.append(change(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))
    return answer