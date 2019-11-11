



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



    def inorder(self):
        pass

    def postorder(self):
        pass


