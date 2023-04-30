def solution(files):
    answer = []
    for i in range(len(files)):
        tmp_idx = []
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                tmp_idx.append(j)
            if tmp_idx and not files[i][j].isdigit():
                break
        answer.append([files[i][:tmp_idx[0]], files[i][tmp_idx[0]:tmp_idx[-1] + 1], files[i][tmp_idx[-1] + 1:]])

    answer = [''.join(x) for x in sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))]
    return answer