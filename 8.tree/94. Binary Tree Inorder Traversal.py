
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题目是求树的中序遍历：即左->根->右，通过queue队列完成
    首先求出树的最左子树，然后从最左子树开始后的每个节点，分别求每个node的左子树和右子树，则构成左->根->右
    Runtime: 36 ms, faster than 71.51% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 13.8 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
