

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    题目需求扣除重复项，即从头到尾遍历，当前一项等于后面项，就跳过继续，直到遍历完即返回
    Runtime: 20 ms, faster than 99.89% of Python online submissions for Remove Duplicates from Sorted List.
    Memory Usage: 11.8 MB, less than 49.30% of Python online submissions for Remove Duplicates from Sorted List.
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