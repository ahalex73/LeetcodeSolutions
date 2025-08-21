class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n log n)
        # Space: O(n)

        # Max heap version

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if (y < x):
                heapq.heappush(stones, y - x)
            
        return -heapq.heappop(stones) if stones else 0

