class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time: O(n^2) 
        # Space: O(n^2)
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        # Memorize the list of prevRows
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows

        # Add numbers in the center
        for i in range(1, numRows - 1):
            # Calculate new Row value
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        
        return prevRows
