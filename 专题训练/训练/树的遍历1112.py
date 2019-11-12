

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class TreeTravel:
    def preorder(self,root):
        res = []
        self.pre_helper(root,res)
        return res

    def pre_helper(self,root,res):
        if root:
            res.append(root.val)
            self.pre_helper(root.left,res)
            self.pre_helper(root.right,res)

    def inorder(self,root):
        res = []
        self.in_helper(root,res)
        return res

    def in_helper(self,root,res):
        if root:
            self.in_helper(root.left,res)
            res.append(root.val)
            self.in_helper(root.left,res)

    def postorder(self,root):
        res = []
        self.post_helper(root,res)
        return res

    def post_helper(self,root,res):
        if root:
            self.post_helper(root.left,res)
            self.post_helper(root.right,res)
            res.append(root.val)

    def preorder_stack(self,root):
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    def inorder_stack(self,root):
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


    def postorder_stack(self,root):
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