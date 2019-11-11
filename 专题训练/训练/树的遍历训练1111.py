



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

    def pre_helper(self,root, res):
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
            self.in_helper(root.right, res)

    def postorder(self,root):
        res = []
        self.post_helper(root, res)
        return res

    def post_helper(self,root,res):
        if root:
            self.post_helper(root.left,res)
            self.post_helper(root.right,res)
            res.append(root.val)


