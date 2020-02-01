




class Solution:
    def sumNumbers(self,root):
        if not root:return
        queue = [(root,root.val)]
        res = 0
        while queue:
            node,val = queue.pop()
            if not node.left and not node.right:
                res += val
            if node.right:

                queue.append((node.right,val * 10 + node.right.val))
            if node.left:
                queue.append((node.left,val * 10 + node.left.val))
        return res


class Solution2:
    def sumNumbers(self,root):
        self.res = 0
        self.dfs(root,0)
        return self.res


    def dfs(self,root,value):
        if root:
            self.dfs(root.left,value * 10+root.val)
            self.dfs(root.right,value * 10+root.val)
            if not root.left and not root.right:
                self.res += value * 10 + root.val