class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1

        curr_num = 0

        while(top <= bottom and left <= right):
            # Traverse to the right         (left -> right)
            for col in range(left, right + 1):
                curr_num += 1
                matrix[top][col] = curr_num

            top += 1
            
            # Traverse to the bottom        (top -> bottom on rightside)
            for row in range(top, bottom + 1):
                curr_num += 1
                matrix[row][right] = curr_num
            
            right -= 1
            
            # Traverse to the left (if any) (right -> left on bottom)
            if(top <= bottom):
                for col in range(right, left - 1, -1):
                    curr_num += 1
                    matrix[bottom][col] = curr_num
            
            bottom -= 1

            # Traverse to the top  (if any) (bottom -> top on left side)
            if (left <= right):
                for row in range(bottom, top - 1, -1):
                    curr_num += 1
                    matrix[row][left] = curr_num

            left += 1

        return matrix
