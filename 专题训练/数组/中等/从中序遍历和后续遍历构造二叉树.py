

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    跟105同样的解法
    Runtime: 216 ms, faster than 18.43% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 85.5 MB, less than 11.47% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    """
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:len(postorder) - 1])
        return root