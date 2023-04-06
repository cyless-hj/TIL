class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        while matrix:
            answer += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    answer.append(row.pop())
            
            if matrix:
                answer += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for i in range(len(matrix) - 1, -1, -1):
                    answer.append(matrix[i].pop(0))
        return answer