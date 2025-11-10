from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(nums: List[int], target: int):
            ent = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        ent = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ent

        def search_right(nums: List[int], target: int):
            ent = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        ent = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ent

        return [search_left(nums, target), search_right(nums, target)]

sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(sol.searchRange(nums = [1, 2], target = 1))
print(sol.searchRange(nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9], target = 8))
print(sol.searchRange(nums = [1], target = 1))

