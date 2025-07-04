class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        write_index = 1 # keeps track of where the next unique number should go.  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


