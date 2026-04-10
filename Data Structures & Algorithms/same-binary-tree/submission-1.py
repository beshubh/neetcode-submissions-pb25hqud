# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(tree1, tree2):
            q1, q2 = deque[TreeNode](), deque[TreeNode]()
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            q1.append(tree1)
            q2.append(tree2)
            while q1 and q2:
                node1, node2 = q1.pop(), q2.pop()
                if node1.val != node2.val:
                    return False
                if node1.left:
                    if node2.left is None:
                        return False
                    q1.append(node1.left)
                if node1.right:
                    if node2.right is None:
                        return False
                    q1.append(node1.right)

                if node2.left:
                    q2.append(node2.left)
                if node2.right:
                    q2.append(node2.right)
            return not q1 and not q2

        return bfs(p, q)
