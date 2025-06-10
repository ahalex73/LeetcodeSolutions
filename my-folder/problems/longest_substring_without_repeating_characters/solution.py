class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max_substring = 0
        stack = []

        for index, val in enumerate(s):
            if val in stack:
                while val in stack:
                    stack.pop(0)
            
            stack.append(val)
            curr_max_substring = max(curr_max_substring, len(stack))

        return curr_max_substring
