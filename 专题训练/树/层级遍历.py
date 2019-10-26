# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意求一棵树的层级遍历，通过BFS来完成

    queue的概念用deque来实现，popleft() 时间复杂为O(1)即可
    外围的While用来定义BFS的终止条件，所以我们最开始initialize queue的时候可以直接把root放进去
    在每层的时候，通过一个cur_level记录当前层的node.val，size用来记录queue的在增加子孙node之前大小，因为之后我们会实时更新queue的大小。
    当每次从queue中pop出来的节点，把它的左右子节点放进Queue以后，记得把节点本身的的value放进cur_level
    for loop终止后，就可以把记录好的整层的数值，放入我们的return数组里。

    Runtime: 16 ms, faster than 95.21% of Python online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 12.2 MB, less than 88.00% of Python online submissions for Binary Tree Level Order Traversal.
    """

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root: return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res


class Solution2(object):
    """
    DFS遍历
    Runtime: 20 ms, faster than 79.17% of Python online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 12.5 MB, less than 22.06% of Python online submissions for Binary Tree Level Order Traversal.
    """

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)