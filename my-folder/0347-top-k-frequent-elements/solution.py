class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n log k)
        # Space: O(n)

        heap = []
        freq = {} 

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        res = []

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res
