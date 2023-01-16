def solution(files):
    answer = []
    sl_list = []

    for i in range(len(files)):
        tmp_idx = []
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                tmp_idx.append(j)
            if tmp_idx and not files[i][j].isdigit():
                break
        head = files[i][:tmp_idx[0]]
        number = files[i][tmp_idx[0]:tmp_idx[-1] + 1]
        tail = files[i][tmp_idx[-1] + 1:]
        sl_list.append([head, number, tail])

    sl_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    sl_list = [''.join(x) for x in sl_list]

    answer = sl_list
    return answer