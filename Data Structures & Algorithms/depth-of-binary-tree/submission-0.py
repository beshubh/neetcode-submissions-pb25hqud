# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(tree: Optional[TreeNode]) -> int:
            if tree is None:
                return 0

            return 1 + max(depth(tree.left), depth(tree.right))

        return depth(root)
