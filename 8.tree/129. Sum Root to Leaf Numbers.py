

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题意是求树每条路径的和，而每条路径得到的数就是从根到叶节点
    用dfs实现，整体思路和113 path sum一致，不过这里的path和是利用value*10+node.right/left.value的值
    Runtime: 36 ms, faster than 86.76% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.
    """
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:return 0
        stack,res = [(root,root.val)],0
        while stack:
            node,value = stack.pop()
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
        return res



class Solution2:
    """
    BFS，但感觉只是用queue重新实现了DFS，区别不大
    Runtime: 40 ms, faster than 58.70% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 14.1 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.
    """
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    queue.append((node.left, value*10+node.left.val))
                if node.right:
                    queue.append((node.right, value*10+node.right.val))
        return res


class Solution3:
    """
    Runtime: 40 ms, faster than 58.70% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 14.1 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.
    """
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value * 10 + root.val)
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value * 10 + root.val)
            if not root.left and not root.right:
                self.res += value * 10 + root.val