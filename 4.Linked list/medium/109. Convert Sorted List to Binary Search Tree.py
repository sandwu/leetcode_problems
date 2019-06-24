# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    题意是将有序链表转为二叉树，因为没有要求二叉树是有序的，所以相对简单很多。
    先依次将链表的值插入列表，最后利用递归直接根据长度的一半生成二叉树即可，效率也是非常快
    Runtime: 100 ms, faster than 99.58% of Python online submissions for Convert Sorted List to Binary Search Tree.
    Memory Usage: 23.9 MB, less than 38.87% of Python online submissions for Convert Sorted List to Binary Search Tree.
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls) - 1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start + end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid - 1)
        root.right = self.helper(ls, mid + 1, end)
        return root

class Solution2(object):
    """
    解法二则是定义快慢指针，快指针定位结尾，慢指针定位中间，然后根据中间和头部分别生成树的右边和左边，可以说和第一种差别不大
    Runtime: 120 ms, faster than 64.52% of Python online submissions for Convert Sorted List to Binary Search Tree.
    Memory Usage: 18.1 MB, less than 99.23% of Python online submissions for Convert Sorted List to Binary Search Tree.
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root