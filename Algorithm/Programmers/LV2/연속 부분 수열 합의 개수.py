def solution(elements):
    answer = 0
    total = set()
    for i in range(len(elements)):
        for j in range(1, len(elements) + 1):
            if i + j < len(elements):
                total.add(sum(elements[i:i + j]))
            else:
                total.add(sum(elements[j:] + elements[:i + j -len(elements)]))
    answer = len(total)
    return answer