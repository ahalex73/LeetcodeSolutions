class Solution:
    def reverseString(self, s: List[str]) -> None:
       # Time: O(n)
       # Space: O(1)
        
        lp = 0
        rp = len(s) - 1

        if(rp) == 0:
            return s 

        while lp <= rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1
        
        return s
