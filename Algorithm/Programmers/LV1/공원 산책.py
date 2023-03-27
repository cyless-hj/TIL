def solution(park, routes):
    answer = []
    move = {'N': [0, -1], 'S': [0, 1], 'W': [-1, 0], 'E': [1, 0]}
    len_x, len_y = len(park[0]), len(park)
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                y, x = i, j
                break
    for route in routes:
        direct, dist = route[0], int(route[2])
        dx, dy = move[direct]
        new_x, new_y = x, y
        for _ in range(dist):
            if 0 <= new_x + dx < len_x and 0 <= new_y + dy < len_y and park[new_y + dy][new_x + dx] != "X":
                new_x, new_y = new_x + dx, new_y + dy
            else:
                new_x, new_y = x, y
                break
        x, y = new_x, new_y
    answer = [y, x]
    return answer