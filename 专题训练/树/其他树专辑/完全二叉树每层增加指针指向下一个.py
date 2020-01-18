

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self,root):
        if not root:return
        if root.right:#因为是完全二叉树，所以右节点存在则左节点一定存在
            root.left.next = root.right
            while root.next: #if parent has next,child's next is paranet next's left
                root.right.next = root.next.left
        self.connect(root.left) #循环遍历剩下的
        self.connect(root.right)
