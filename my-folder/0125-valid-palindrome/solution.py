class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)

        l = 0
        r = len(s) - 1

        while(l < r):
            
            # Skip the non-alphnumeric characters from the left pointer
            while(l < r) and not self.isAlphaNum(s[l]):
                l += 1
            
            # Skip the non-alphanumeric characters from the right pointer 
            while(r > l) and not self.isAlphaNum(s[r]):
                r -= 1
            
            # Verify that the opposing characters are equal to be a palindrome
            if(s[l].lower() != s[r].lower()):
                return False
            
            l += 1
            r -= 1
        
        return True
            
    def isAlphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
