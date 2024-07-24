class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 ==0 and x != 0):
            return False

        reserved_half = 0
        primer = x

        while x != 0:
            last_num = x % 10
            reserved_half = reserved_half * 10 + last_num
            x = x // 10
        if reserved_half == primer:
            return True
        return False