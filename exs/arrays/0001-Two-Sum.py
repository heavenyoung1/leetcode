from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in seen:
                return [seen[check], i]
            seen[num] = i


solution = Solution()
print(solution.twoSum(nums = [11, 2, 11,9, 7], target = 9))
