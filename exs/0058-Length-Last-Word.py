class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split()[-1]
        return len(last_word)


sol = Solution()
print((sol).lengthOfLastWord(s = "Hello World"))