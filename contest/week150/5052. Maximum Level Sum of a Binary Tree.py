# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题意是求树的最大层级和，返回对应的层级
    通过BFS将每层的层级和求出，然后指定最大和变量max，最后返回最大和所对应的层级index即可
    """
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        if not root: return []
        queue, res, ans, index = deque([root]), 0, 0, 1

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            sum1 = sum(cur_level)
            print(sum1)
            if sum1 > res:
                res = sum1
                ans = index
            index += 1

        return ans

