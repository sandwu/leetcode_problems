


"""
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

class TreeNode:
    def __init__(self,x):
        self.val = x

class Solution:
    def buildTree(self,preorder, inorder):
        if len(preorder) == 0:return None
        if len(preorder) == 1:return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root















