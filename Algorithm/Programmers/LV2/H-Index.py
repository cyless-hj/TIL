def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    index = list(range(1, len(citations) + 1))
    print(citations)
    print(index)
    for i in range(len(citations)):
        if citations[i] >= index[i]:
            answer = index[i]
    return answer