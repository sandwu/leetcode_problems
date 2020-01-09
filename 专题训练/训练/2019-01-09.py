


class Solution:
    def isvalid(self,root):
        res = []
        res = self.inorder(root,res)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return False

    def inorder(self,root,res):
        if not root:return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

    def generateTrees(self,n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i] = dp[j] * dp[i-j-1]
        return dp.pop()

    def generateTreesbyLists(self,n):
        if n == 0:
            return []
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result