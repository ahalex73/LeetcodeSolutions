class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # m = row
        # n = col
        # indices represents a 0-indexed location to perform some increment operations on the matrix
        
        """First take the indices [0,1], here 0 represent the 0th row and 1 represent the 1st column so it will first increment the values of 0th row then the inital matrix become [[1,1,1],[0,0,0]] and then it will increment the values of 1st column then the initial matrix become [[1,2,1], [0,1,0]]
Similarly for other indices [1,1], here it will increment the values of 1st row then inital matrix become [[1,2,1], [1,2,1]] then it will increment the value of 1st column then the inital matrix become [[1,3,1], [1,3,1]]
Now the no. of odd values are 6 in this matrix so output will be 6"""

        """ Example
            m = 2                     ->      row_increments = [1,1]
            n = 3                     ->      col_increments = [0,2,0]
            indices = [[0,1],[1,1]]   ->

            Then check if each cell is odd
                Cell (0,0): 1+0=1 → odd ✅
                Cell (0,1): 1+2=3 → odd ✅
                Cell (0,2): 1+0=1 → odd ✅
                Cell (1,0): 1+0=1 → odd ✅
                Cell (1,1): 1+2=3 → odd ✅
                Cell (1,2): 1+0=1 → odd ✅
        """

        # Track how many times each row and column is incremented
        row_increments = [0] * m
        col_increments = [0] * n

        for r, c in indices:
            row_increments[r] += 1
            col_increments[c] += 1

        # Count cells that are odd
        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (row_increments[i] + col_increments[j]) % 2 == 1:
                    odd_count += 1

        return odd_count

