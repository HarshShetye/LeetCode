class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiraled = []
        while matrix:
            spiraled += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    spiraled.append(row.pop())
            if matrix:
                spiraled += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiraled.append(row.pop(0))
        return spiraled