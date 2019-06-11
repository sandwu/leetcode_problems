
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    遍历整个链表，如果发现与给的值相等，则跳过该值。要注意的是需要定义一个新的节点，新的节点指针指向head，这样方便
    使用pre.next = head.next跳向下一个节点
    Runtime: 56 ms, faster than 94.33% of Python online submissions for Remove Linked List Elements.
    Memory Usage: 18.6 MB, less than 61.78% of Python online submissions for Remove Linked List Elements.
    """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = pre = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return new_head.next

class Solution2(object):
    """
    定义快慢指针来完成，思路和上述的还是挺像的，区别是概念上的，快指针负责遍历，遇到相同的跳过，遇到不同的让慢指针的值等于
    快指针的值，同时慢指针继续遍历。
    Runtime: 56 ms, faster than 94.33% of Python online submissions for Remove Linked List Elements.
    Memory Usage: 18.6 MB, less than 61.78% of Python online submissions for Remove Linked List Elements.
    """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
            fast = fast.next
        slow.next = None
        return new_head.next
