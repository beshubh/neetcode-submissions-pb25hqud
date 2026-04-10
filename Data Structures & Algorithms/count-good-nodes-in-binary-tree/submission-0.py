# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(tree, max_encountered):
            nonlocal ans
            if tree is None:
                return 
            if tree.val >= max_encountered:
                ans += 1
                max_encountered = tree.val
            
            dfs(tree.left, max_encountered)
            dfs(tree.right, max_encountered)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return ans + 1
            
            

