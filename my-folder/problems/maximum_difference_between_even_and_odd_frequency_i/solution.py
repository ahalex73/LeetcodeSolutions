class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        
        for char in s:
            if char in freq:
                freq[char] = freq.get(char, 0) + 1

            else:
                freq[char] = 1
        
        min_even = float('inf')
        max_odd = float('-inf')

        for count in freq.values():
            if count % 2 == 0:
                min_even = min(min_even, count)
            else:
                max_odd = max(max_odd, count)

        return max_odd - min_even