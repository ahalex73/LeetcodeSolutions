class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(mat)
        midpoint = 0
        total_sum = 0

        if (n % 2 == 1):
            # It is an even nxn matrix - no midpoint
            mid = n // 2
            midpoint = mat[mid][mid]

        for i in range(n):
            # Primary diagonal
            total_sum += mat[i][i] 

            # Secondary diagonal
            total_sum += mat[i][n - i - 1]

        # Remove duplicate entries if the matrix has a midpoint
        total_sum -= midpoint

        return total_sum

