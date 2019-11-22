



class TreeTravel:
    def pre_order(self,root):
        res = []
        self.pre_helper(root,res)
        return res

    def pre_helper(self,root,res):
        if root:
            res.append(root.val)
            self.pre_helper(root.left,res)
            self.pre_helper(root.right,res)

    def in_order(self,root):
        res = []
        self.in_helper(root,res)
        return res

    def in_helper(self,root,res):
        if root:
            self.in_helper(root.left,res)
            res.append(root.val)
            self.in_helper(root.right,res)

    def post_order(self,root):
        res = []
        self.post_helper(root,res)
        return res

    def post_helper(self,root,res):
        if root:
            self.post_helper(root.left,res)
            self.post_helper(root.right,res)
            res.append(root.val)



class TreeTravel2:
    def pre_order(self,root):
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            #当没有节点的时候，说明树已经遍历完了
            if not node:
                return res
            #将根节点加入，再依次加入右、左节点，这样下一波循环先pop出来的是左节点
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)


    def in_order(self,root):
        res,stack = [],[]
        while stack:
            #将root直接依次找到最左边的节点，都加到stack中
            while root:
                stack.append(root)
                root = root.left
            #然后取出最左的节点加入结果集，在将该节点的右节点也加入stack，方便后续遍历
            node = stack.pop()
            if not node:
                return res
            res.append(node.val)
            root = node.right

    def post_order(self,root):
        #直接参考前序遍历，从根左右变成根右左，区别在于把res颠倒就行
        res,stack = [],[]
        stack.append(root)
        while stack:
            node =stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]