
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    给出树的前序遍历和中序遍历推导树原来的样子，先定位到root的index，然后递归查找左子树和右子树即可
    Runtime: 188 ms, faster than 36.05% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    Memory Usage: 85.4 MB, less than 15.96% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.buildTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
        return root


class Solution2(object):
    """
    简化了上面的解法，因为前序遍历的第一个数一定就是递归的下一个根节点，利用这一点即可写出更简洁的代码
    Runtime: 116 ms, faster than 65.52% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    Memory Usage: 50 MB, less than 53.78% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root