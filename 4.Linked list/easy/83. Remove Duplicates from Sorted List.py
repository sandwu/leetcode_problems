


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    理解链表的node.next=node.next.next即可，即让链表的下一位指向下下位，则表示跳过中间的那位重复数
    Runtime: 28 ms, faster than 96.60% of Python online submissions for Remove Duplicates from Sorted List.
    Memory Usage: 11.7 MB, less than 92.84% of Python online submissions for Remove Duplicates from Sorted List
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head