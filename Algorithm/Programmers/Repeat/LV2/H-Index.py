def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    print(citations)
    for idx, citation in enumerate(citations):
        if idx + 1 <= citation:
            answer = idx + 1
    return answer