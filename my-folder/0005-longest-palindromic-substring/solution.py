class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
            # You iterate through each character of the string as a potential center → O(n).
            # For each center, you expand outward to check for a palindrome. In the worst case (string is all the same character),
            # this expansion can take up to O(n) steps.
            # You do this twice per index (once for odd-length, once for even-length palindromes).
        # Space: O(1)
        
        start, end = 0, 0 # Keeping track of longest palindrome indicies

        def expand_from_center(l, r) -> tuple[int, int]:
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            
            return l + 1, r - 1

        for i in range(len(s)):
            odd_left, odd_right = expand_from_center(i, i)
            even_left, even_right = expand_from_center(i, i + 1)

            if odd_right - odd_left > end - start:
                start, end = odd_left, odd_right
            
            if even_right - even_left > end - start:
                start, end = even_left, even_right
            
        return s[start:end + 1]
                
