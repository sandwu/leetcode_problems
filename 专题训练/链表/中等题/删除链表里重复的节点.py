
#82


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    题意是要删除重复项，指定两个节点指向head，然后判断当前head和head.next值是否相等，相等则继续；
    整体的思路是比较清晰的，就是指针的指向相对比较复杂
    Runtime: 32 ms, faster than 64.44% of Python online submissions for Remove Duplicates from Sorted List II.
    Memory Usage: 11.7 MB, less than 70.21% of Python online submissions for Remove Duplicates from Sorted List II.
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = dummy = ListNode(0)
        tmp.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                dummy.next = head
            else:
                dummy = dummy.next
                head = head.next

        return tmp.next