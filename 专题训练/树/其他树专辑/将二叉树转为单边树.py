


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def revert(self,root):
        res = []
        self.preorder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]

    def preorder(self, root, res):
        if not root: return
        res.append(root)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

class Solution2:
    def flatten(self,root):
        if not root:return
        left = root.left
        right = root.right
        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left
        while root.right:
            root = root.right
        root.right = right