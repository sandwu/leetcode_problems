

#230

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self,root,k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self,root): #中序遍历获取排序后的结果
        if not root:return None
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)

