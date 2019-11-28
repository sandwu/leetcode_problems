
#141

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    定义快慢指针，快的一次走两格，慢的一次走一格，只要有环肯定能相遇
    Runtime: 40 ms, faster than 95.00% of Python online submissions for Linked List Cycle.
    Memory Usage: 18.1 MB, less than 78.85% of Python online submissions for Linked List Cycle.
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
