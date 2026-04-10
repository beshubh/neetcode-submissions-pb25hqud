# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def get_ancestors(tree, t):
            res = []
            while tree:
                if tree.val == t.val:
                    res.append(t)
                    return res

                res.append(tree)
                if t.val < tree.val:
                    tree = tree.left
                else:
                    tree = tree.right
            return res

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


