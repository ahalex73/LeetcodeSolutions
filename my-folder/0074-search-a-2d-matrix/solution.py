class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1 # Theoretically flatten the 2D matrix

        while l <= r:
            mid = (l + r) // 2
            i = mid // cols
            j = mid % cols
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False
