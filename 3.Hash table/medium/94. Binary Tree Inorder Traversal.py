# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    """
    中序遍历，即先获取左子树的结果，再根节点，再右子树，思路还是很清晰
    Runtime: 12 ms, faster than 99.66% of Python online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 11.8 MB, less than 5.78% of Python online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


class Solution2(object):
    """
    iteratively,即用迭代的思路来完成该题，整体和上述差别不大
    Runtime: 16 ms, faster than 98.85% of Python online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 11.8 MB, less than 5.78% of Python online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res,stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right