class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Time: O(n^2) - however it is O(n/2) for half as many accesses using a midpoint
        # Space: O(1)
        # In place solution

        for row in image:
            lp = 0
            rp = len(row) - 1

            while lp <= rp:
                if lp == rp:
                    row[lp] ^= 1

                row[lp], row[rp] = row[rp], row[lp]
                row[lp] ^= 1
                row[rp] ^= 1

                lp += 1
                rp -= 1

        return image
                
