# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -10000
        def dfs(root) -> int:
            nonlocal global_max
            if root is None:
                return -10000
            left, right = dfs(root.left), dfs(root.right)
            max_path_sum = max(root.val, root.val + left, root.val + right, root.val + left + right)
            global_max = max(global_max, max_path_sum)
            return max(root.val, root.val + left, root.val + right)
            
        dfs(root)
        return global_max
