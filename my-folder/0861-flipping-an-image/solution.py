class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Time: O(n^2)
        # Space: O(1)
        # NIAVE SOLUTION

        # Flip the image horizonatally - reverse the array
        for row in image:
            # Reverse the row in-place
            row.reverse()
            
            # Flip each bit using XOR
            for col in range(len(row)):
                row[col] ^= 1

        return image

                
