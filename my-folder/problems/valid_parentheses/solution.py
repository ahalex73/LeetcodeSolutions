class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
        }
        stack = []

        for char in s:
            if char in valid_dict:

                # If we don't have a starting (, [, or { char in the stack before trying to append a closing symbol, return False
                if not stack or stack[-1] != valid_dict[char]:
                    return False
                stack.pop()
            
            else:
                stack.append(char)

        return not stack # True if empty, false if not