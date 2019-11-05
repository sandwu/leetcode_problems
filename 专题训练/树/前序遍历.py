

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是求树的前序遍历(即根-->左--->右)。在栈的领域当然用栈来完成！
    这里需要注意的就是要先往栈加入右子树，然后再是左子树，这样在出栈的时候就是先左子树，然后右子树！
    Runtime: 12 ms, faster than 95.51% of Python online submissions for Binary Tree Preorder Traversal.
    Memory Usage: 11.7 MB, less than 74.55% of Python online submissions for Binary Tree Preorder Traversal.
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return None
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res


class Solution2(object):
    """
    递归完成左右子树的遍历，要注意的是基线条件返回是[]，然后左子树、右子树的增加需要用extend
    Runtime: 8 ms, faster than 99.35% of Python online submissions for Binary Tree Preorder Traversal.
    Memory Usage: 11.8 MB, less than 63.67% of Python online submissions for Binary Tree Preorder Traversal.
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res