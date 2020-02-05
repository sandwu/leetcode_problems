

class Solution:
    def sumroot(self,root):
        self.res = 0
        self.dfs(root,0)
        return self.res

    def dfs(self,root,value):
        if root:
            self.dfs(root.left,value*10+root.val)
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val


class Solution2:
    def sumroot2(self,root):
        if not root:return
        queue = [(root,root.val)]
        res = 0
        while queue:
            node,val = queue.pop()
            if not node.right and not node.left:
                res += val
            if node.right:
                queue.append((node.right,val*10 + node.right.val))
            if node.left:
                queue.append((node.left,val*10 + node.left.val))

        return res


class Solution3:
    def pathsum(self,root,sum):
        if not root:return
        self.res = []
        self.dfs(root,root.val,[root.val],sum)
        return self.res

    def dfs(self,root,val, path,sum):
        if root:
            self.dfs(root.left,val+root.left.val, path + root.left.val,sum)
            self.dfs(root.right, val+root.left.val, path + root.right.val,sum)
            if not root.left and not root.right and val==sum:
                self.res.append(path)



class Solution4:
    def pathsum(self,root,sum):
        if not root:return
        res = []
        queue = [(root,root.val,[root.val])]
        while queue:
            node,val,path = queue.pop()
            if val == sum and not node.left and not node.right:
                res.append(path)
            if node.left:
                queue.append((node.left, node.left.val+val, path+node.left.val))
            if node.right:
                queue.append((node.right, node.right.val + val, path + node.right.val))


class Solution5:
    def revert(self,root):
        if not root:return
        left = root.left
        right = root.right
        root.left = None
        self.revert(left)
        self.revert(right)
        root.right = left
        while root.right:
            root = root.right
        root.right = right

    def revert2(self,root):
        if not root:return
        res = self.preorder(root,[])
        for i in range(len(res)):
            res[i].left = None
            res[i].right = res[i+1]

    def preorder(self,root,res):
        if root:
            res.append(root.val)
            self.preorder(root.left,res)
            self.preorder(root.right,res)
        return res



class Solution6:
    def connect(self,root):
        if not root:return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)






