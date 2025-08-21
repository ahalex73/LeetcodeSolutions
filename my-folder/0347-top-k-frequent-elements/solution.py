class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n log k)
        # Space: O(n)

        heap = []
        freq = {} 

        for i in nums:
            freq[i] = 1 + freq.get(i, 0) # O(n)
        
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key)) # O(log n)
        
        res = []

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])  # O(log n)
        
        return res
