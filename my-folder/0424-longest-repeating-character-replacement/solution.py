class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 

        l = 0
        maxFrequency = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # Increment found letter
            maxFrequency = max(maxFrequency, count[s[r]])        # gather our maximum frequency character

            while((r - l + 1) - maxFrequency > k):      # WindowSize = (r - l + 1)
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)   # Our window size is what were finding length from

        return res
                
