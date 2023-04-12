# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    long = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def check(root):
            if not root:
                return -1
            left = check(root.left)
            right = check(root.right)

            self.long = max(self.long, left + right + 2)
            return max(left, right) + 1
        check(root)
        return self.long