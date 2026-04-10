# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            cur_res = []
            nodes = deque()
            while q:
                node = q.pop()
                cur_res.append(node.val)
                if node.left: nodes.appendleft(node.left)
                if node.right: nodes.appendleft(node.right)

            q = nodes
            res.append(cur_res)
        return res