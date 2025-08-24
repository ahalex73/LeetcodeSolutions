class Solution:
    def reorganizeString(self, s: str) -> str:
        # Time: O(n log k) n - total number of characters and k is unique number of characters
        # Space: O(n) -> O(k) for freq, O(k) for max_heap, and O(n) for res such that O(n + k) turns into O(n)  
        
        freq = {}
        # O(n)
        for c in s:
            freq[c] = 1 + freq.get(c, 0) 
        
        max_heap = [(-freq, char) for char, freq in freq.items()]
        heapq.heapify(max_heap)

        res = []

        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq += 1
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq, char

        if len(res) != len(s):
            return ""
        
        return "".join(res)


