class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Time: O(n + n) -> O(n)
        # Space: O(1) considering we would have O(9) possible numbers
        
        freq = {}
        largest_lucky = -1

        for i in arr:
            freq[i] = 1 + freq.get(i, 0)
        
        for key, val in freq.items():
            if key == val:
                largest_lucky = max(largest_lucky, val)
        
        return largest_lucky
