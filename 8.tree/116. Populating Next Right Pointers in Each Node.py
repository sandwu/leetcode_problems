"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    """
    题意是将完全二叉树转为每层的链表，
    解法通过两个判断，第一个判断是否有右子树，如果有则左子树指向右子树；第二个判断本身是否指向下一个，如果有，
    则需要把右子树再指向本身下一个的左子树，按题来说就是先2->3,然后5->6
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)




class Solution2(object):
    """
    Runtime: 52 ms, faster than 75.03% of Python online submissions for Populating Next Right Pointers in Each Node.
    Memory Usage: 14.1 MB, less than 84.00% of Python online submissions for Populating Next Right Pointers in Each Node.
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue = [root]
        while queue:
            level = queue
            queue = []
            while level:
                node = level.pop(0)
                if not level:
                    node.next = None
                else:
                    node.next = level[0]
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return root