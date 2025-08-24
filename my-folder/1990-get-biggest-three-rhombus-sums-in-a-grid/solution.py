class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Time: O(n^4)
        # Space: O(1) - stores at most 3 elements

        def calc_rhombus_sum(left, right, up, down):
            curr_sum = 0
            c1 = c2 = (left + right) // 2
            expand = True
            for row in range(up, down + 1):
                if c1 == c2:
                    curr_sum += grid[row][c1]
                else:
                    curr_sum += grid[row][c1] + grid[row][c2]
                
                if c1 == l:
                    expand = False
                
                if expand:
                    c1 -= 1
                    c2 += 1
                else:
                    c1 += 1
                    c2 -= 1

            return curr_sum

        m = len(grid)
        n = len(grid[0])
        priority_q = []

        for i in range(m):
            for j in range(n):
                r = j
                l = r
                d = i

                while l >= 0 and r <= n - 1 and d <= m - 1: 
                    rhombus_sum = calc_rhombus_sum(l, r, i, d)

                    # Update priority queue immediately
                    if rhombus_sum not in priority_q:
                        if len(priority_q) < 3:
                            heapq.heappush(priority_q, rhombus_sum)
                        else:
                            if rhombus_sum > priority_q[0]:
                                heapq.heappop(priority_q)
                                heapq.heappush(priority_q, rhombus_sum)

                    # Expand rhombus
                    l -= 1
                    r += 1
                    d += 2
                
        priority_q.sort(reverse=True)

        return priority_q
