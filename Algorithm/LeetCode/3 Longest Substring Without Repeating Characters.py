from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        answer = 0

        for i in s:
            if i not in queue:
                queue.append(i)
            else:
                idx = queue.index(i)
                for j in range(idx + 1):
                    queue.popleft()
                queue.append(i)
            answer = max(answer, len(queue))
        return answer