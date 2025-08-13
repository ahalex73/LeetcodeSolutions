class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Time: O(k + (m x n)) - k = number of operations from indicies matrix
        # Space: O(m x n)
        # m - rows
        # n - cols

        row_count = [0] * m
        col_count = [0] * n

        # Get the counts of each operation per index
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        # Find which indices are odd or even
                # row_count = [1, 1]
                # col_count = [0, 2, 0]
        odd_count = 0

        for r in range(m):
            for c in range(n):
                if((row_count[r] + col_count[c]) % 2 == 1):
                    odd_count += 1 

        return odd_count
