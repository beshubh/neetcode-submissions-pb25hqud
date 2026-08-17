# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        order = []
        def go(root):
            nonlocal order
            if not root:
                order.append('#')
                return
            order.append(str(root.val))
            go(root.left)
            go(root.right)
        go(root)
        return ','.join(order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        order = data.split(',')
        i = 0
        def build():
            nonlocal i
            if i >= len(order):
                return None
            if order[i] == '#':
                i += 1
                return None
            root = TreeNode(int(order[i]))
            i += 1
            root.left = build()
            root.right = build()
            return root
        return build()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))