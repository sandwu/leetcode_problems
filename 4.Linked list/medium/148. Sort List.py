# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    题意是对链表排序，用归并排序来做链表，也是相当易懂的
    Runtime: 236 ms, faster than 52.04% of Python online submissions for Sort List.
    Memory Usage: 26.3 MB, less than 65.08% of Python online submissions for Sort List.
    """
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next

        tail.next = h1 or h2

        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

    def sortList2(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        l = self.sortList(head)
        r = self.sortList(slow)

        return self.merge(l, r)
