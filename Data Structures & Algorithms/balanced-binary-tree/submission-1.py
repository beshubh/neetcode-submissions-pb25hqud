# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(tree: Optional[TreeNode]) -> int:
            if tree is None:
                return 0
            return 1 + max(depth(tree.left), depth(tree.right))

        is_balanced: list[bool] = []

        def balanced(tree: TreeNode | None) -> int:
            if tree is None:
                return 0
            left_height, right_height = 0, 0
            if tree.left:
                left_height = 1 + balanced(tree.left)
            if tree.right:
                right_height = 1 + balanced(tree.right)

            is_balanced.append(abs(left_height - right_height) <= 1)
            return max(left_height, right_height)

        balanced(root)
        return all(is_balanced)
