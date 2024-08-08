# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = []

        while p or stack_p or q or stack_q:
            while p:
                stack_p.append(p)
                p = p.left
            while q:
                stack_q.append(q)
                q = q.left

            if len(stack_p) != len(stack_q):
                return False

            p = stack_p.pop()
            q = stack_q.pop()

            if p.val != q.val:
                return False

            p = p.right
            q = q.right

        return True