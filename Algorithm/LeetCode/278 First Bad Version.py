class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid
        return start