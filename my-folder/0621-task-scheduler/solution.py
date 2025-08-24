class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(T log k) number of tasks 
        # Space: O(k) -> cooldown + O(k) freq + O(k) for max_heap 

        freq = Counter(tasks)
        max_heap = [(-count) for count in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    # Send duplicate tasks to the dungeon!
                    cooldown.append((time + n, count))
            
            if cooldown and cooldown[0][0] == time:
                _, ready_count = cooldown.popleft()
                heapq.heappush(max_heap, ready_count)
            
        return time





