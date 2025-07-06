class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Sliding window solution
        # Time: O(n)
        # Space: O(1)

        needleLength = len(needle)
        haystackLength = len(haystack)

        if needleLength == 0:
            return 0  
        
        window_word = haystack[:needleLength]

        if needleLength > haystackLength:
            return -1

        for i in range(haystackLength - needleLength + 1):
            window_word = haystack[i:i + needleLength]
            if window_word == needle:
                return i
        
        return -1
