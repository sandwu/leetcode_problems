

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def preorder(self,root):
        self.res = []
        self.prehelper(root)
        return self.res

    def prehelper(self,root):
        if not root:return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorder2(self,root):
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)


    def inorder(self,root):
        res,stack = [],[]
        while stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res



    def postorder(self,root):
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]