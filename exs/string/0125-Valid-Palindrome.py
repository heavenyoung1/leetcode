

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = (''.join(i for i in s if i.isalnum())).lower()
        return True if cleaned == cleaned[::-1] else False


sol = Solution()
print(sol.isPalindrome('A man, a plan, a canal: Panama'))