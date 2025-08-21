class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        
        for i in range(len(nums)):
            nums[i] *= -1
        
        # Create a max heap
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return -heapq.heappop(nums)

