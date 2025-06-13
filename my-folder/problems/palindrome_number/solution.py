class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_digit = str(x)
        reversed_string = string_digit[::-1]

        return string_digit == reversed_string
        
