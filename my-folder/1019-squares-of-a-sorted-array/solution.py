class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1

        # Start in reverse - at our greatest number in nums
        for i in range((len(nums) - 1), -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1

        return res
