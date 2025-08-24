class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        left = 0
        zeros = 0
        max_width = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_width = max(max_width, right - left) # Typically window size is r - l + 1
        
        return max_width


