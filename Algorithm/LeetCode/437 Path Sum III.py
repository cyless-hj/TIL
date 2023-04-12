# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, targetSum):
            res = 0
            if not root:
                return res

            if targetSum == root.val:
                res += 1
            
            res += dfs(root.left, targetSum - root.val)
            res += dfs(root.right, targetSum - root.val)

            return res
        
        if not root:
            return 0
        
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)