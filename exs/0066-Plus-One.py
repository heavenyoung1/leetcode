class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 0:
                digits[i] += 1
                return digits
            else:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                elif digits[i] != 0:
                    return digits
        if set(digits) == {0}:
            digits.insert(0, 1)
            return digits
        else:
            return digits

