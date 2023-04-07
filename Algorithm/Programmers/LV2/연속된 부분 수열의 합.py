def solution(sequence, k):
    answer = []
    sequence = [0] + sequence
    total = [0] * len(sequence)
    
    start, end = 1, 1
    a, b = -1, -1
    ln = int(1e9)
    
    for i in range(1, len(sequence)):
        total[i] = total[i - 1] + sequence[i]

    while start <= end < len(sequence):
        tmp = total[end] - total[start - 1]
        if tmp < k:
            end += 1
        elif tmp == k:
            if ln > end - start:
                ln = end - start
                a, b = start, end
            end += 1
        else:
            start += 1
    answer = [a - 1, b - 1]
    return answer