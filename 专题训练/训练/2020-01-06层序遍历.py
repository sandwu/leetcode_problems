


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self,root):
        from collections import deque
        if not root: return []
        queue,res = deque(),[]
        queue.append(root)
        while queue:
            cur_level,size = [],len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

    def dfs(self,root):
        self.res = []
        level = 0
        self.helper(root,level)
        return self.res

    def helper(self,root,level):
        if not root:return []
        if len(self.res) < level+1:
            self.res.append([])
        self.res[level].append(root.val)
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)
