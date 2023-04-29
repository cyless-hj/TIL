def solution(dirs):
    directs = {'U': [1, 0], 'D': [-1, 0], 'R': [0, 1], 'L': [0, -1]}
    route = set()
    x, y = 0, 0
    for d in dirs:
        nx, ny = x + directs[d][0], y + directs[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            route.add(str(x) + str(y) + str(nx) + str(ny))
            route.add(str(nx) + str(ny) + str(x) + str(y))
            x, y = nx, ny
    return len(route) // 2