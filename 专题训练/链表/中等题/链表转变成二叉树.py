

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self,head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        pre, slow, fast = None, head, head #通过pre定位到slow的上一个，方便树的左子树调用
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        pre.next = None
        root.left = self.sortedListToBST(head)
        return root
