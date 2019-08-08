



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    题意是将BST原地转化为单右边树，解题思路是递归将左子树全部转化为右子树，然后再将右子树全部转化为最右边树
    详细图解如下，要注意的是每次遍历到左子树也节点后，就会返回然后走右子树，然后将此时的root.right=left，
    即图解的第三步，因为此时root.right=left，所以要判断left的右子树是否结束，即用while来循环将left走完，最后
    再赋值回右子树
     1
      \
   2   5
    \   \
 3   4   6

     1
      \
   2   5
    \   \
 3   4   6

      1
      \
   2   5
    \   \
     3   6
      \
       4

     1
      \
       2
        \
         3
          \
           4
            \
             5
              \
               6


    Runtime: 16 ms, faster than 96.41% of Python online submissions for Flatten Binary Tree to Linked List.
    Memory Usage: 12.1 MB, less than 73.53% of Python online submissions for Flatten Binary Tree to Linked List.
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left
        while root.right:
            root = root.right
        root.right = right


class Solution2(object):
    """
    取巧的方法，即先前序遍历，然后直接在列表里修改
    Runtime: 24 ms, faster than 62.28% of Python online submissions for Flatten Binary Tree to Linked List.
    Memory Usage: 12.1 MB, less than 72.00% of Python online submissions for Flatten Binary Tree to Linked List
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]

    def preOrder(self, root, res):
        if not root: return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)