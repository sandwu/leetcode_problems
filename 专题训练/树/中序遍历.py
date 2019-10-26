



class Solution(object):
    """
    leetcode 94
    """
    def inorderTraversal(self, root):
        res,stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right