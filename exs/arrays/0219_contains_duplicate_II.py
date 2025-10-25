from typing import List

# 26 мс
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        original = {}
        for i in range(len(nums)):
            if nums[i] in original and (i - original[nums[i]]) <= k:
                return True
            original[nums[i]] = i
        return False

sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,4, 5, 6, 7, 1], 1))

