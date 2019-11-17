
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



class TreeTravel:
    def pretravel(self,root):
        res = []
        self.prehelp(root,res)
        return res

    def prehelp(self,root,res):
        if root:
            res.append(root.val)
            self.prehelp(root.left,res)
            self.prehelp(root.right,res)


    def pre_order(self,root):
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    def in_order(self,root):
        pass


    def post_order(self,root):
        pass