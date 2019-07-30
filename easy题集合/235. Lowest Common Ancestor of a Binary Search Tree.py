

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    题意是求BST的两个节点的最小父节点
    解法通过判断是否在同一颗子节点树下来进行的，核心逻辑就是，如果两个在同一个子节点树，则继续迭代；如果不是，则返回该子节点的node值；
    所以迭代中的q.val-root.val也等价于p.val-root.val，一切只是服务于判断其中一个节点位于的位置，然后再while里判断两个节点的位置
    Runtime: 72 ms, faster than 57.99% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 20 MB, less than 38.44% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[q.val > root.val]
        return root



class Solution2(object):
    """
    迭代的思路要好于上者，即也是通过root值是否同时大于或小于q，p的值来判断是否在同棵子树，是的话就继续迭代，不是就返回根节点
    Runtime: 68 ms, faster than 76.94% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 19.9 MB, less than 55.49% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        next = p.val < root.val > q.val and root.left or \
           p.val > root.val < q.val and root.right
        return self.lowestCommonAncestor(next, p, q) if next else root