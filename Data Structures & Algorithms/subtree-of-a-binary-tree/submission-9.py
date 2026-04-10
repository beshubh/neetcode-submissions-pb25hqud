# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root is None:
            return False

        def is_subtree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            
            if tree1.val == tree2.val:
                return is_subtree(tree1.left, tree2.left) and is_subtree(tree1.right, tree2.right)
            return False
        if is_subtree(root, subRoot) or is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)