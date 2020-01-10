
"""

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    题意是列出给出的数字范围内的所有BST集合
    利用树的迭代完成
    Runtime: 44 ms, faster than 48.10% of Python online submissions for Unique Binary Search Trees II.
    Memory Usage: 15.6 MB, less than 27.68% of Python online submissions for Unique Binary Search Trees II.
    """
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n+ 1)


    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result