class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Time: O(n x m)
        # Space: O(n x m)
        
        # Rotate matrix - boxGrid[::-1] reverses every row, * unpacks each row and is passed to zip 
        #                               to get the transpose by connecting rows to columns

        rotated = [list(row) for row in zip(*boxGrid[::-1])]
        rows, cols = len(rotated), len(rotated[0])

        for c in range(cols):
            bot = rows - 1
            curr_row = rows - 1

            while curr_row >= 0:
                if rotated[curr_row][c] == "*":
                    # If an obstacle, reset bottom pointer above the obstacle
                    bot = curr_row - 1

                elif rotated[curr_row][c] == "#":
                    if curr_row != bot:
                        # We have a stone, apply gravity
                        rotated[curr_row][c] = "."
                        rotated[bot][c] = "#"
                    bot -= 1
                
                curr_row -= 1 # Do nothing if its an empty space

        return rotated

