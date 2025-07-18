class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Time: O(n log n  + m log m)
        # Space: O(1)

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while(child < len(g) and cookie < len(s)):
            if(g[child] <= s[cookie]):
                child += 1
            
            cookie += 1
        
        return child
