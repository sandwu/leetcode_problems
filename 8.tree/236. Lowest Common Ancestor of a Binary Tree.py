



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    题意是求树的最小祖先，即两个节点最靠近叶子节点的祖先，如果两个节点是同一颗子树，则祖先是其中的一个节点
    解法直接递归求左子树和右子树，如果两者同时存在，则说明祖先是二者的父节点。如果左子树存在，右子树不存在，则
    祖先就是左子树对应的root。
    要注意的是递归终止条件，即当root==p or root==q就说明找到了对应的节点，而not root也返回root，则说明没有找到，
    此时返回的root即是None
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
