class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time: O(n^2)
        # Space: O(1)

        n = len(matrix)

        # 1. Perform a transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # 2. Perform a horizontal flip 
        for row in matrix:
            row.reverse()
        

