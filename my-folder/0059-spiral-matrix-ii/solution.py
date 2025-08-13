class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Time: O(m x n)
        # Space: O(m x n)
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        curr_num = 0
        
        while top <= bottom and left <= right:
            # Traverse top row (left → right)
            for col in range(left, right + 1):
                curr_num += 1
                matrix[top][col] = curr_num
            top += 1
            
            # Traverse right column (top → bottom)
            for row in range(top, bottom + 1):
                curr_num += 1
                matrix[row][right] = curr_num
            right -= 1
            
            # Traverse bottom row (right → left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    curr_num += 1
                    matrix[bottom][col] = curr_num
                bottom -= 1
            
            # Traverse left column (bottom → top)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    curr_num += 1
                    matrix[row][left] = curr_num
                left += 1
        
        return matrix
