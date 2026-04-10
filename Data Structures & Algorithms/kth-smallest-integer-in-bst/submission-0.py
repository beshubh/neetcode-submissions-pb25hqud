# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        def inorder(tree):
            nonlocal traversal
            if tree is None:
                return None
            
            inorder(tree.left)
            traversal.append(tree.val)
            inorder(tree.right)
        inorder(root)
        if len(traversal) < 1:
            return -1 
        return traversal[k - 1]


