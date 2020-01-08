
#98


class Solution:
    def isvalid(self,root):
        self.res = []
        self.inorder(root)
        for i in range(1, len(self.res)):
            if self.res[i] <= self.res[i - 1]:
                return False
        return True

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
