



class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.get_res(root,res,sum,[root.val])
        return res

    def get_res(self, curr, res, target, path):
        if not curr:return None
        if sum(path)==target and not curr.left and not curr.right:
            res.append(path)
        if curr.left:
            self.get_res(curr.left,res,target,path+[curr.left.val])
        if curr.right:
            self.get_res(curr.right,res,target,path+[curr.right.val])


class Solution2:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        queue = [(root,root.val,[root.val])]
        while queue:
            curr,val,path = queue.pop()
            if val == sum and not curr.left and not curr.right:
                res.append(path)
            if curr.left:
                queue.append((curr.left,curr.left.val+val,path+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, curr.right.val + val, path + [curr.right.val]))
        return res