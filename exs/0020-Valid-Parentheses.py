class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys():
                if not stack or stack[-1] != brackets[i]:
                    return False
                stack.pop()

        return not stack