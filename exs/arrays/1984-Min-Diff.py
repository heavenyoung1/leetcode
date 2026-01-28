from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sort = sorted(nums)
        gl_min = 99999999999
        for i in range((len(sort) - k + 1)):
            diffirence = sort[i + k - 1] - sort[i]
            if diffirence < gl_min:
                gl_min = diffirence

        return gl_min