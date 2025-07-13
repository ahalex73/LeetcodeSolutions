class Solution:
    def processStr(self, s: str, k: int) -> str:
        # clever reverse simulation/index mapping approach
        length = 0
        for ch in s:
            if ch.islower():
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
        
        if k >= length:
            return '.'

        for i in reversed(range(len(s))):
            ch = s[i]
            if ch.islower():
                if k == length - 1:
                    return ch
                length -= 1
            elif ch == '*':
                if length < 10**15:
                    length += 1
                if k == length - 1:
                    pass
            elif ch == '#':
                length //= 2
                if k >= length:
                    k -= length
            elif ch == '%':
                k = length - 1 - k

        return '.'

