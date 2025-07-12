class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        l = 0
        r = len(numbers) - 1
        while(l < r):
            curr_sum = numbers[l] + numbers[r]
            if(curr_sum == target):
                return [l + 1, r + 1]
            
            elif(curr_sum < target):
                l += 1
            else:
                r -= 1
        return False
            


