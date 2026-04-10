# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def lca(root, p, q):
            if p.val == root.val or q.val == root.val:
                return root
            
            if p.val < root.val and q.val < root.val:
                return lca(root.left, p, q)
            elif p.val >= root.val and q.val >= root.val:
                return lca(root.right, p, q)
            else:
                return root
        return lca(root, p, q)


