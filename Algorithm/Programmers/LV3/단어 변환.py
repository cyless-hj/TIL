def solution(begin, target, words):
    answer = 100
    visited = [False for _ in range(len(words))]
    
    def dfs(start, target, idx):
        nonlocal visited, answer, words
        if start == target:
            answer = min(answer, idx)
        else:
            for i in range(len(words)):
                cnt = 0
                for j in range(len(start)):
                    if start[j] != words[i][j]:
                        cnt += 1
                if visited[i] == False and cnt == 1:
                    visited[i] = True
                    dfs(words[i], target, idx + 1)
    dfs(begin, target, 0)
    if answer == 100:
        answer = 0
    return answer