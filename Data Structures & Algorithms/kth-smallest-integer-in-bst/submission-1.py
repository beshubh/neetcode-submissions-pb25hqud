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
            stack = [tree]
            while stack:
                if stack[-1] is None:
                    while stack and stack[-1] is None:
                        stack.pop()
                    if not stack:
                        continue
                    root = stack.pop()
                    traversal.append(root.val)
                    stack.append(root.right)
                else:
                    stack.append(stack[-1].left)
        inorder(root)
        if len(traversal) < 1:
            return -1 
        return traversal[k - 1]


