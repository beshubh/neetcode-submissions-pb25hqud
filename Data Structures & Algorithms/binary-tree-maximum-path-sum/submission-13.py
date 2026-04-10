# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -100000
        def dfs(root):
            nonlocal global_max
            if root is None:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            cur_max = max(root.val, root.val + left + right, root.val + left, root.val + right)
            global_max = max(cur_max, global_max)
            return max(root.val, root.val + left, root.val + right)
        
        dfs(root)
        return  global_max

            
