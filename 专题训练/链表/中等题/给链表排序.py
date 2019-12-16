

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self,head):
        if not head or not head.next:
            return head

        pre,slow,fast = None,head,head
        while fast and fast.next:
            pre,slow,fast = slow,slow.next,head.next.next
        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left,right)

    def merge(self,left,right):
        curr = dummy = ListNode(0)
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