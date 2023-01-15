from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_trees = list(map(list, skill_trees))

    for arr in skill_trees:
        arr = deque(arr)
        s = ''
        for j in range(len(arr)):
            v = arr.popleft()
            if v in skill:
                s += v

        if skill.startswith(s):
            answer += 1

    return answer