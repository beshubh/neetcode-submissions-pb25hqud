# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        buf = []
        def preorder(root):
            if root is None:
                buf.append('nil')
                return
            buf.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(buf)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        buf = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if buf[i] == 'nil':
                i += 1
                return None
            
            node = TreeNode(int(buf[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

