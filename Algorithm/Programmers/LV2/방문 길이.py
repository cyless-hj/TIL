def solution(dirs):
    answer = 0
    arr = []
    coord = [0, 0]
    for move in dirs:
        tmp = list(coord)
        if move == 'U':
            coord[1] += 1
        elif move == 'D':
            coord[1] -= 1
        elif move == 'L':
            coord[0] -= 1
        elif move == 'R':
            coord[0] += 1
        
        if coord[0] <= 5 and coord[0] >= -5 and coord[1] <= 5 and coord[1] >= -5:
            arr.append(''.join(list(map(str, [coord[0], coord[1], tmp[0], tmp[1]]))))
            arr.append(''.join(list(map(str, [tmp[0], tmp[1], coord[0], coord[1]]))))
        else:
            coord = tmp

    answer = len(set(arr)) // 2
    return answer