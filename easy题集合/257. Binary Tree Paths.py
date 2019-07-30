
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是求二叉树的从根节点到叶子节点的路径，即有多少个叶节点就有多少的路径
    用迭代的方式完成，基线是每次判断是否到根节点，是的话就加入到结果，不是的话就继续迭代，把ls对应的加上即可
    Runtime: 20 ms, faster than 69.29% of Python online submissions for Binary Tree Paths.
    Memory Usage: 11.7 MB, less than 96.24% of Python online submissions for Binary Tree Paths.
    """
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root ,"" ,res)
        return res

    def dfs(self ,root ,ls ,res):
        if not root.left and not root.right:
            res.append(ls +str(root.val))
        if root.left:
            self.dfs(root.left ,ls +str(root.val ) +"->" ,res)
        if root.right:
            self.dfs(root.right ,ls +str(root.val ) +"->" ,res)

#另外附上dfs和bfs的解法

# dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.right:
            stack.append((node.right, ls + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, ls + str(node.val) + "->"))
    return res


# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.left:
            queue.append((node.left, ls + str(node.val) + "->"))
        if node.right:
            queue.append((node.right, ls + str(node.val) + "->"))
    return res