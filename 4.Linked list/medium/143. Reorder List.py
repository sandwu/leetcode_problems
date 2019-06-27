
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    For linked list 1->2->3->4-5, the code first makes the list to be 1->2->3->4<-5 and 4->None, then make 3->None,
    for even number linked list: 1->2->3->4, make first 1->2->3<-4 and 3->None, and lastly do not forget to make 2->None.
    Runtime: 84 ms, faster than 84.57% of Python online submissions for Reorder List.
    Memory Usage: 29.5 MB, less than 93.87% of Python online submissions for Reorder List.
    """
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # ensure the first part has the same or one more node
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        p = slow.next
        slow.next = None
        node = None
        while p:
            nxt = p.next
            p.next = node
            node = p
            p = nxt
        # combine head part and node part
        p = head
        while node:
            tmp = node.next
            node.next = p.next
            p.next = node
            p = p.next.next #p = node.next
            node = tmp