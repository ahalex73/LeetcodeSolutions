class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Step 1: Rotate 90° clockwise
        # reverse rows + transpose
        rotated = [list(row) for row in zip(*boxGrid[::-1])] # boxGrid[::-1] is reversing row elements and then * before boxGrid is unpacking
                                                             #               into rows, then zip is putting them into columns
        rows, cols = len(rotated), len(rotated[0])

        # Step 2: Apply gravity column by column
        for col in range(cols):
            write = rows - 1  # bottom-most available spot
            
            for row in range(rows - 1, -1, -1):
                if rotated[row][col] == '*':
                    write = row - 1  # reset "floor" above obstacle
                
                elif rotated[row][col] == '#':
                    if row != write:  # move stone down
                        rotated[row][col] = '.'
                        rotated[write][col] = '#'
                    write -= 1  # next available slot is above

        return rotated

