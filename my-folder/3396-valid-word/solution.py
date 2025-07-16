class Solution:
    def isValid(self, word: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        if len(word) < 3:
            return False

        vowel_set = "aeiouAEIOU"
        vowels = 0
        consonants = 0

        for c in word:
            if c.isalpha():
                if c in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False
            
        return vowels >= 1 and consonants >= 1
