class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Time: O(n)
        # Space: O(1)

        snake_r, snake_c = 0, 0 
        
        for i in commands:
            if i == "RIGHT":
                snake_c += 1
            
            if i == "LEFT":
                snake_c -= 1

            if i == "UP":
                snake_r -= 1

            if i == "DOWN":
                snake_r += 1
            
        return (snake_r * n) + snake_c  # Think of each row of 4 in a 4x4 matrix, then add the columns 
                                        # to get the index. Makes a lot of sense.
