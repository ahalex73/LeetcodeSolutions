class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        triangle = self.build_triangle(rowIndex + 1)
        return triangle[-1]

    def build_triangle(self, rows):
        if rows == 0:
            return []
        if rows == 1:
            return [[1]]

        prevRow = self.build_triangle(rows - 1)
        nextRow = [1] * rows

        # Generate new row
        for i in range(1, rows - 1):
            nextRow[i] = prevRow[-1][i - 1] + prevRow[-1][i]
        # Return the last entry

        prevRow.append(nextRow)

        return prevRow


