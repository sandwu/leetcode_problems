
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是求BST中第k小的树
    BST即binary search tree，树节点满足左子树小于该节点小于右子树，所以中序遍历后就可以得到有序列表
    中序遍历即：左子树→根节点→右子树，所以根据中序遍历写得递归代码如下
    Runtime: 52 ms, faster than 42.88% of Python online submissions for Kth Smallest Element in a BST.
    Memory Usage: 19.8 MB, less than 5.44% of Python online submissions for Kth Smallest Element in a BST.
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self ,Node):
        if not Node:
            return
        self.helper(Node.left)
        self.k -= 1
        if self.k == 0:
            self.res = Node.val
            return self.res
        self.helper(Node.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    """
    用非递归的方法来实现，利用到栈的数据结构
    先遍历到树底，依次将左子树的所有节点压入栈，最后栈顶存放的就是最小的数，然后依次从栈推出，
    当k位于左子树的时候直接返回值即可，如果不在左子树，那就继续将右子树压入栈
    Runtime: 44 ms, faster than 77.44% of Python online submissions for Kth Smallest Element in a BST.
    Memory Usage: 19.6 MB, less than 63.94% of Python online submissions for Kth Smallest Element in a BST.
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right