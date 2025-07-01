class Solution:
    def possibleStringCount(self, word: str) -> int:
        length = len(word)
        count = length

        for i in range(1, length):
            if word[i] != word[i - 1]:
                count -= 1

        return count


