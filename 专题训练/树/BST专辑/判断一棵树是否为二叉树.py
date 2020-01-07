
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是验证一棵树是否为BST，BST满足左子树小于根小于右子树，所以中序遍历后必然是有序的
    先中序遍历，然后判断是否是有序的即可
    Runtime: 32 ms, faster than 83.45% of Python online submissions for Validate Binary Search Tree.
    Memory Usage: 16.7 MB, less than 25.77% of Python online submissions for Validate Binary Search Tree.
    """
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root ,output)

        for i in range(1 ,len(output)):
            if output[i] <= output[ i -1]:
                return False
        return True

    def inOrder(self ,root ,output):
        if not root:
            return None

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)