from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = set(nums)
        return True if len(nums) != len(original) else False


# Мое решение, 19мс, но там есть еще 1мс
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
