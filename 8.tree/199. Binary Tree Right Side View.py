


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    题意是从右边看一棵树，返回你能看到的全部
    递归实现，要考虑几种情况：
        1.最左边左子树高于右子树，则要先返回最左边左子树
        2.最右边右子树下的左子树高于右子树
        3.右子树或者左子树刚好成一排
    解法：先得到最右、最左子树，然后返回结果：root.val+右子树+多出的左子树
    Runtime: 36 ms, faster than 83.42% of Python3 online submissions for Binary Tree Right Side View.
    Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]


class Solution2:
    """
    DFS解法，可以说非常巧妙了，核心就在于depth == len(view)
    通过这个条件牢牢把握上述的三种情况，当左子树低于最右边时，即不满足depth==len(view)
    而每当遍历到的节点，depth高于当前的depth：即len(view)，就添加到结果集，因为递归是从右到左，
    所以肯定会从右到左的加入节点
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view