class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
