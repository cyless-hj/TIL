def solution(wallpaper):
    answer = []
    s_x = 51
    s_y = 51
    x = 0
    y = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < s_x:
                    s_x = i
                if j < s_y:
                    s_y = j
                if i > x:
                    x = i
                if j > y:
                    y = j
    answer = [s_x, s_y, x + 1, y + 1]
    return answer