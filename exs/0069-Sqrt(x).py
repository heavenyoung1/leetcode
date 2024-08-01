class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            if mid * mid > x:
                right = mid - 1
            if mid * mid == x:
                return mid
        return right