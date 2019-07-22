
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    """
    题意是每次从二叉搜索树里通过next返回最小值，通过stack来完成
    根据BST左子树小于根节点小于右子树的规则，可以一开始拿到最左的树节点，然后判断其右子树是否存在，存在即
    加入栈，等待下次的取其左子树的值；不存在则直接取上一层的左子树的值
    Runtime: 76 ms, faster than 61.56% of Python online submissions for Binary Search Tree Iterator.
    Memory Usage: 21.2 MB, less than 79.90% of Python online submissions for Binary Search Tree Iterator.
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        while root:
            self.s.append(root)
            root = root.left


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.s.pop()
        x = node.right
        while x:
            self.s.append(x)
            x = x.left
        return node.val



    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.s ) >0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()