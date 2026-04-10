# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_trees(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if not tree1 or not tree2 or tree1.val != tree2.val:
                return False

            return same_trees(tree1.left, tree2.left) and same_trees(tree1.right, tree2.right)

        def subtree_inner(tree: Optional[TreeNode], subtree: Optional[TreeNode]):
            if tree is None and subtree is None:
                return True

            if subtree is None:
                return True
            if tree is None:
                return False

            if same_trees(tree, subtree):
                return True
            return subtree_inner(tree.left, subtree) or subtree_inner(tree.right, subtree)

        return subtree_inner(root, subRoot)

