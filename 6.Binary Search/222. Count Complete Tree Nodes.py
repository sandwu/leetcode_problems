
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是求完全二叉树的节点数，参考博文：https://www.cnblogs.com/yrbbest/p/4993469.html
    完全二叉树即是除了最后一行节点不满，其他都是满的，而且最后一行是从左至右依次满的；满二叉树则是子节点要么满要么不满，
    该解法就是利用二者特性来做的，先定义一个求树高度的函数(求高度往左子树找)，然后分别求得左子树和右子树的高度，如果二者相等，则左子树是
    满二叉树，右子树是完全二叉树；如果不等，则右子树是满二叉树，左子树是完全二叉树
    Runtime: 64 ms, faster than 98.26% of Python online submissions for Count Complete Tree Nodes.
    Memory Usage: 27.7 MB, less than 57.43% of Python online submissions for Count Complete Tree Nodes.
    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        while root:
            l ,r = map(self.getHeight ,(root.left ,root.right))
            if l== r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left
        return count

    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height