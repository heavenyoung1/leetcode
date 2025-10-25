from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_n = nums[0]
        max_diff = 0
        for i in nums:
            if i < min_n:
                min_n = i
            if (i - min_n) > max_diff:
                max_diff = i - min_n
        return max_diff if max_diff != 0 else -1

sol = Solution()
print(sol.maximumDifference(nums=[7,1,5,4]))
print(sol.maximumDifference(nums=[9,4,3,2]))