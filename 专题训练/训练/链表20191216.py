
class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def partitionList(self,head,x):
        l1 = h1 = ListNode(None)
        l2 = h2 = ListNode(None)
        while head:
            if head.val <= x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = h2.next
        l2.next = None
        return h1.next


    def convertLinkListToBST(self,head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        pre.next = None
        root.left = self.convertLinkListToBST(head)
        root.right = self.convertLinkListToBST(slow.next)
        return root

    def sortLinkList(self,head):
        """merge sort"""
        if not head:
            return None
        if not head.next:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        right = self.sortLinkList(slow)
        left = self.sortLinkList(head)
        return self.merge(left, right)

    def merge(self, left, right):
        curr = dummy = ListNode(None)
        while left and right:
            if left.val <= right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = left or right
        return curr.next

    def fromNthRotateLink(self,head, k):
        dummy = curr = head
        n = 0
        prev = None
        while dummy:
            prev = dummy
            dummy = dummy.next
            n += 1

        if not n or not k % n:
            return head

        for _ in range(n - k%n -1):
            curr = curr.next
        res = curr.next
        prev.next = head
        curr.next = None
        return res

    def removeDuplicateNode(self,head):
        curr = dummy = ListNode(None)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head.next = head.next.next
                head = head.next
                dummy.next = head
            else:
                head = head.next
                dummy = dummy.next
        return curr.next

    def rotateLinkListFromMTON(self,head,m,n):
        dummy = res = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            dummy = dummy.next

        prev = None
        reverse = dummy.next
        for _ in range(n - m + 1):
            curr = reverse
            reverse = reverse.next
            curr.next = prev
            prev = curr  # 到最后reverse位于n的后一位，prev位于n

        dummy.next.next = reverse
        dummy.next = prev

        return res.next

    def sumTwoLinkList(self,l1,l2):
        pass

    def swapTwoLinkList(self,head):
        pass


