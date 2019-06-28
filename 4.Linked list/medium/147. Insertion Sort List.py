# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """

    Runtime: 156 ms, faster than 81.60% of Python online submissions for Insertion Sort List.
    Memory Usage: 15.1 MB, less than 78.57% of Python online submissions for Insertion Sort List.
    """
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val: # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val: # classic insertion sort to find position
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next # insert
        return dummy.next