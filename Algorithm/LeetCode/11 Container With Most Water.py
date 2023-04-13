class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        answer = 0
        while end - start > 0:
            answer = max(answer, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return answer