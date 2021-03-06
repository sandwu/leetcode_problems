
# 145. Binary Tree Postorder Traversal



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res[::-1]

    def helper(self,root,res):
        if root:
            res.append(root.val)
            self.helper(root.left,res)
            self.helper(root.right,res)