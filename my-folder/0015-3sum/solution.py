class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2)
        # Space: O(1) / O(n) in some languages
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if (i > 0) and  nums[i] == nums[i - 1]:
                # If we have a duplicate leftmost element, skip over it
                continue
            
            l = i + 1
            r = len(nums) - 1
        
            while(l < r):
                curr_sum = a + nums[l] + nums[r]

                if(curr_sum > 0):
                    r -= 1
                elif(curr_sum < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1

        return res
