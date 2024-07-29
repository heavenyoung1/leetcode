class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[write_index]:
                write_index += 1
                nums[write_index] = nums[i]
        return write_index + 1