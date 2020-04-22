


class Solution:
    def preorder(self,root):
        self.pre_res = []
        self.pre_help(root)
        return self.pre_res

    def pre_help(self,root):
        if not root:return
        self.pre_res.append(root.val)
        self.pre_help(root.left)
        self.pre_help(root.right)

    def inorder(self,root):
        self.in_res = []
        self.in_help(root)
        return self.in_res

    def in_help(self,root):
        if not root:return
        self.in_help(root.left)
        self.in_res.append(root.val)
        self.in_help(root.right)

    def postorder(self,root):
        self.post_res = []
        self.post_helper(root)
        return self.post_res

    def post_helper(self,root):
        if not root:return
        self.post_helper(root.left)
        self.post_helper(root.right)
        self.post_res.append(root.val)



class Solution2:
    def bfs_pre(self,root):
        if not root:return
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res

    def bfs_in(self,root):
        res,stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def bfs_post(self,root):
        post_res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node: continue
            post_res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return post_res[::-1]








