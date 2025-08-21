class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(n log k)
        # Space: O(n)
        
        origin = (0,0)

        heap = []
        
        # Gather the distance from all of the points
        for point in points:
            distance = self.distance(origin, point)
            heapq.heappush(heap, (distance, point))

        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result

    def distance(self, point1: List[int], point2: List[int]) -> float:
        x1, y1 = point1
        x2, y2 = point2

        return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
