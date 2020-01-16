# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

class Solution(object):
    """
    题意是求树从根节点到叶节点之间的路径和等于所给的sum值的所有集合
    利用dfs即递归回溯算法完成
    Runtime: 40 ms, faster than 43.75% of Python online submissions for Path Sum II.
    Memory Usage: 18 MB, less than 68.85% of Python online submissions for Path Sum II.
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.dfs(root, sum, res, [root.val])
        return res

    def dfs(self, root, target, res, path):
        if not root: return
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
        if root.left:
            self.dfs(root.left, target, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, target, res, path + [root.right.val])


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    """
    同样的可以用BFS来完成，即每次都把每一层的所有结果放入
    Runtime: 48 ms, faster than 13.69% of Python online submissions for Path Sum II.
    Memory Usage: 14.2 MB, less than 86.49% of Python online submissions for Path Sum II.
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))
        return res


