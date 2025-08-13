class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        
        if n <= 0:
            return False

        res = math.log10(n) / math.log10(3)
        return abs(res - round(res)) < 1e-10
