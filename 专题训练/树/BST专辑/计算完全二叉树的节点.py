



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self,root):
        if not root:return 0
        left,right = map(self.getHeight, (root.left,root.right))
        if left==right:return 2 ** left + self.countNodes(root.right)
        else:return 2** right + self.countNodes(root.left)

    def getHeight(self,root):
        height = 0
        while root:
            height += 1
            root = root.left #左子树求最大的高度
        return height



class Solution2:
    def preorder(self,root):
        res = []
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if not root:
            return None
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right,res)

    def inorder(self,root):
        pass

    def postorder(self,root):
        pass