
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    """
    题意是反转树，左子树和右子树交换
    DFS：用栈完成，将每个节点的左子树和右子树得到后反转放入栈等待下次的调用
    Runtime: 8 ms, faster than 99.49% of Python online submissions for Invert Binary Tree.
    Memory Usage: 11.8 MB, less than 52.81% of Python online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root



class Solution2(object):
    """
    BFS：用队列实现
    Runtime: 20 ms, faster than 51.32% of Python online submissions for Invert Binary Tree.
    Memory Usage: 11.8 MB, less than 70.78% of Python online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

class Solution3(object):
    """
    直接迭代完成
    Runtime: 8 ms, faster than 99.49% of Python online submissions for Invert Binary Tree.
    Memory Usage: 11.7 MB, less than 96.78% of Python online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root