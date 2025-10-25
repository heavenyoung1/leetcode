from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = set(nums)
        return True if len(nums) != len(original) else False


# Мое решение, 19мс, но там есть еще 1мс
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))

# Вот это решение занимает 7мс
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = set()
        for i in nums:
            if i in original:
                return True
            else:
                original.add(i)
        return False
    

sol1 = Solution1()
print(sol1.containsDuplicate([1,2,3,1]))
print(sol1.containsDuplicate([1,2,3,4]))

# Решение при помощи отсортированного массива
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
            
# хех, это решение вообще 53мс, ну оно и понятно, тут сортировка массива
sol2 = Solution2()
print(sol2.containsDuplicate([1,2,3,1]))
print(sol2.containsDuplicate([1,2,3,4]))

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
sol3 = Solution3()
print(sol3.containsDuplicate([1,2,3,1]))
print(sol3.containsDuplicate([1,2,3,4]))