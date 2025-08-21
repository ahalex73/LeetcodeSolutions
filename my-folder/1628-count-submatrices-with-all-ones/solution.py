class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        res = 0
        width = [[0] * cols for _ in range(rows)]

        # Fill in the width array
        # The main goal of the width array is to store, for each cell, the number 
        # of consecutive 1’s to its left, which allows efficient counting of all-1 submatrices
        # ending at that cell.

        for r in range(rows):
            for c in range(cols):
                if mat[r][c]:
                    # If the first index is 0, start the running total
                    if c == 0:
                        width[r][c] = 1
                    else:
                        width[r][c] = 1 + width[r][c - 1]

        # PRINT OUT WIDTH MATRIX   
        # for i in width:
        #     print(i)
        
        # Iterate over each cell - consider it the bottom right corner of the submatrix
        # width[r][c] = maximum width a submatrix ending at (r, c) can be
        # width keeps track of consecutive 1’s in a row 
        #       lets us know the maximum possible width for a submatrix ending at any cell.
        # current_min_width ensures all rows in the rectangle are full of 1’s.
        # up_row iterates upwards from the current row, checking possible heights.
        # Adding current_min_width each iteration counts all valid rectangles ending at (row, col).
        
        for r in range(rows):
            for c in range(cols):
                curr_min_width = width[r][c]
                up_row = r

                while up_row >= 0 and curr_min_width > 0:
                    curr_min_width = min(curr_min_width, width[up_row][c])
                    res = (res + curr_min_width)

                    up_row -= 1
                
        return res

