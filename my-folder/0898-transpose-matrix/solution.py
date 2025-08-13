class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """ In place method - ONLY VISITING THE TOP RIGHT OF THE MATRIX - SKIP diagonals
                            # ONLY WORKS FOR SQUARE MATRIXES
        # Time: O(n^2)
        # Space: O(1)      
        """
        
        # Time: O(n^2)
        # Space: O(n^2)

        rows = len(matrix)
        cols = len(matrix[0])

        transpose_matrix = []
        
        for c in range(cols):        
            new_row = []
            for r in range(rows):    
                new_row.append(matrix[r][c])

            transpose_matrix.append(new_row)

        return transpose_matrix
