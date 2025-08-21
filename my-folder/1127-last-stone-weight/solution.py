class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n^2 log n)
        # Space: O(1)
        # Space: 
        # x and y are stones, y is never lighter compared to x, but can be equal
        # if x != y, the stone of weight x is destroyed (made 0), and the stone of weight y has new weight y - x

        stones.sort()

        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()

            if (x != y):
                stones.append(y - x)    # O(1)
                stones.sort()           # O(n log n)
            
        return stones[0] if stones else 0

            



