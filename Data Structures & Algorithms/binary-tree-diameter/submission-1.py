# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def length(tree: Optional[TreeNode]) -> tuple[int]:
            nonlocal max_diameter
            if tree is None:
                return 0
            left_height, right_height = 0, 0
            if tree.left:
                left_height = 1 + length(tree.left)
            if tree.right:
                right_height = 1 + length(tree.right)

            diameter = left_height + right_height
            max_diameter = max(max_diameter, diameter)
            return max(left_height, right_height)
        
        length(root)
        return max_diameter
