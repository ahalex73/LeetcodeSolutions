import re

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # Time: O(n)   i.e   O(n) + O(n) + O(n) = O(n)
        # Space: O(1)
        
        if len(password) < 8:
            return False

        if (self.contains_special_char(password) != True):
            return False
        
        containsUpper = False
        containsLower = False
        containsDigit = False
        containsDuplicate = self.contains_duplicate(password)

        for i in password:            
            if i.isupper():
                containsUpper = True
            if i.islower():
                containsLower = True
            if i.isdigit():
                containsDigit = True
            
        return (containsUpper and containsLower and containsDigit and containsDuplicate)
        
    # Check for trailing duplicate 
    def contains_duplicate(self, password):
        for i in range(1, len(password)):
            if password[i - 1] == password[i]:
                return False
            
        return True
            

    def contains_special_char(self, s: str) -> bool:
        pattern = r"[!@#$%^&*()\-\+]"
        return bool(re.search(pattern, s))



            
            


            

