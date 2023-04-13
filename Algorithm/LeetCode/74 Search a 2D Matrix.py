class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = sum(matrix, [])
        start, end = 0, len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == matrix[mid]:
                return True
            elif target < matrix[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False