class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n

        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        odd_total = 0

        for r in range(m):
            for c in range(n):
                if((row_count[r] + col_count[c]) % 2 == 1):
                    # The cell is odd
                    odd_total += 1 
                
        return odd_total
