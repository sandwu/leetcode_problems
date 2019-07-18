


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    """
    题意是用之字形遍历树
    用deque可以左边pop出，右边append进去，根据树的特点，先pop出父节点，然后append进去子节点！
    Runtime: 24 ms, faster than 53.71% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    Memory Usage: 12.2 MB, less than 14.06% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            #奇数层要反转结果
            r = r[::-1] if len(res) % 2 else r
            if r:
                res.append(r)
        return res


class Solution2(object):
    """
    用BFS的解法来做，大体思路和前者差不多，不过用了flag*-1来解决奇偶的关系
    Runtime: 20 ms, faster than 75.64% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    Memory Usage: 12 MB, less than 96.82% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res