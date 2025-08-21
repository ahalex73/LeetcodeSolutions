class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n log k)
        # Space: O(1) -> O(k)

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if(num > heap[0]):
                heapq.heappushpop(heap, num) # Push new number and pop smallest
            
        return heap[0]



