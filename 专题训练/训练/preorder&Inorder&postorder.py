

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def preorder_stack(self,root):
        if not root:return
        res  = []
        res.append(root.val)
        res.append(self.preorder(root.left))
        res.append(self.preorder(root.right))
        return res

    def preorder_queue(self,root):
        if not root:return
        res = queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            pass


    def inorder(self):
        pass

    def postorder(self):
        pass
