
#leetcode:94\144\145
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
        res.append(self.preorder_stack(root.left))
        res.append(self.preorder_stack(root.right))
        return res

    def preorder_queue(self,root):
        if not root:return
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


    def inorder(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def inorder2(self,root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def postorder(self,root):
        res = []
        self.helper2(root, res)
        return res

    def helper2(self, root, res):
        if root:
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)

    def postorder2(self,root):
        if not root:return
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]



