class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        l = 0
        r = len(s) - 1

        while l < r:
            # Skip alphanum on left side
            while (l < r) and not self.isAlphaNum(s[l]):
                l += 1

            # Skip alphanum on right side
            while (l < r) and not self.isAlphaNum(s[r]):
                r -= 1

            # While they are equal on each side
            if(s[l].lower() == s[r].lower()):
                l += 1
                r -= 1
            else:
                return False
        return True
            
    def isAlphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
